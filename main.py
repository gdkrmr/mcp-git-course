from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
import json
import os

from rdm_mcp.prompts import wrap_content_in_prompt, introduction_prompt

# @mcp.tool
# def run_git_command(command: list[str]) -> str:
#     """
#     Executes a Git command and returns the output. It is executed in python as

#     ```python
#     subprocess.run(["git"] + command, shell=True, check=True, text=True, capture_output=True)
#     ```

#     Args:
#         command (list[str]): The Git command to execute.

#     Returns:
#         str: The output of the Git command.
#     """
#     import subprocess

#     try:
#         result = subprocess.run(["git"] + command,
#                                 shell=True,
#                                 check=True,
#                                 text=True,
#                                 capture_output=True)
#         return result.stdout.strip()
#     except subprocess.CalledProcessError as e:
#         raise ToolError(f"Failed to execute command '{command}': {e.stderr.strip()}")


STATE_DIR = os.path.join(os.path.dirname(__file__), ".state")
STATE_FILE = os.path.join(STATE_DIR, "state.json")
COURSE_DIR = os.path.join(os.path.dirname(__file__), "resources", "lessons")

class CourseState():
    """
    Manages the state of the Git course, including current lesson and step.
    This class is responsible for initializing, loading, saving, and advancing the course state.
    It reads the course directory to build the initial state and provides methods to advance steps and retrieve content.

    Attributes:
        state (dict): The current state of the course, including current lesson and step.

    Methods:
        build_initial_state() -> dict: Reads the course directory and builds the initial state.
        init_state() -> None: Initializes the state directory and creates the initial state file if it does not exist.
        load_state() -> dict: Loads the course state from the state directory.
        save_state(state: dict) -> None: Saves the current state of the course to the state directory.
        advance_step() -> str: Advances to the next step in the course and returns its content.
        get_current_step_content() -> str: Returns the content of the current step in the course.
    """

    def __init__(self):
        if os.path.exists(os.path.join(STATE_DIR, "state.json")):
            self.state = self.load_state()
        else:
            self.state = self.build_initial_state()


    def set_current_lesson_step(self, lesson_idx: int, step_index: int, has_started: bool) -> None:
        """
        Sets the current lesson and step in the course state.

        Args:
            lesson_idx (int): The index of the lesson to set as current.
            step_index (int): The index of the step to set as current.
        """
        if lesson_idx < 0 or step_index < 0:
            raise Error("Lesson index and step index must be non-negative integers.")

        if lesson_idx >= len(self.state["lessons"]):
            raise Error(f"Lesson index {lesson_idx} is out of range. There are only {len(self.state['lessons'])} lessons.")

        if step_index >= len(self.state["lessons"][lesson_idx]["steps"]):
            raise Error(f"Step index {step_index} is out of range for lesson {lesson_idx}. It has only {len(self.state['lessons'][lesson_idx]['steps'])} steps.")

        self.state["current_lesson"] = lesson_idx
        self.state["current_step"] = step_index
        self.state["has_started"] = has_started
        self.save_state(self.state)


    def build_initial_state(self) -> dict:
        """
        Read course directory and build the initial state for the course.
        """
        # list directories in course dir for lessons, for is e.g. 01_basics
        if not os.path.exists(COURSE_DIR):
            raise ToolError(f"Course directory '{COURSE_DIR}' does not exist.")

        # lessons have the form "01_basics", "02_working-with-branches", etc., we
        # want to extract the lesson names after sorting them.
        lesson_dirs = sorted([d for d in os.listdir(COURSE_DIR) if os.path.isdir(os.path.join(COURSE_DIR, d))])

        # each lesson is a directory, we want to extract the steps, that are of the form 01_step1.md, 01_step2.md, etc.
        lessons = []
        for d in lesson_dirs:
            lesson_dir = os.path.join(COURSE_DIR, d)
            lesson_steps = sorted([s for s in os.listdir(lesson_dir) if s.endswith(".md")])
            lesson_steps = [
                {
                    "name": s.split("_")[1].split(".")[0],
                    "file": s
                }
                for s in lesson_steps
            ]

            lesson = {
                "name": d.split("_")[1],
                "direcory": d,
                "steps": lesson_steps
            }
            lessons.append(lesson)

        return {
            "current_lesson": 0,
            "current_step": 0,
            "has_started": False,
            "lessons": lessons
        }


    def init_state(self):
        """
        Creates the state directory if it does not exist.
        This is used to store the course progress and history.
        """
        if not os.path.exists(STATE_DIR):
            os.makedirs(STATE_DIR)
        if not os.path.exists(STATE_FILE):
            initial_state = self.build_initial_state()
            with open(STATE_FILE, "w") as f:
                json.dump(initial_state, f, indent=4)


    def load_state(self) -> dict:
        """
        Loads the course state from the state directory.

        Returns:
            dict: The current state of the course.
        """
        state_file = os.path.join(STATE_DIR, "state.json")
        if not os.path.exists(state_file):
            raise ToolError(f"State file '{state_file}' does not exist. Please initialize the state first.")

        with open(state_file, "r") as f:
            return json.load(f)


    def save_state(self, state: dict) -> None:
        """
        Saves the current state of the course to the state directory.

        Args:
            state (dict): The current state of the course.
        """
        state_file = os.path.join(STATE_DIR, "state.json")
        with open(state_file, "w") as f:
            json.dump(state, f, indent=4)


    def advance_step(self) -> str:
        """
        Advances the current step in the course state.

        Args:
            state (dict): The current state of the course.

        Returns:
            str: The content for the next step in the course or an indication that the course is complete.
        """
        if not self.state["has_started"]:
            self.state["has_started"] = True
            self.save_state(self.state)
            return introduction_prompt
        else:
            current_lesson = self.state["current_lesson"]
            current_step = self.state["current_step"]
            lesson = self.state["lessons"][current_lesson]

            if current_step < len(lesson["steps"]) - 1:
                current_step += 1
            else:
                if current_lesson < len(self.state["lessons"]) - 1:
                    current_step = 0
                    current_lesson += 1
                else:
                    return "You have completed the course! Congratulations!"

            self.state["current_step"] = current_step
            self.state["current_lesson"] = current_lesson
            self.save_state(self.state)

            return self.get_current_step_content()


    def get_current_step_content(self) -> str:
        """
        Returns the content of the current step in the course.

        Returns:
            str: The content of the current step.
        """
        current_lesson = self.state["current_lesson"]
        current_step = self.state["current_step"]
        lesson = self.state["lessons"][current_lesson]
        step = lesson["steps"][current_step]

        step_path = os.path.join(COURSE_DIR, lesson["direcory"], step["file"])
        with open(step_path, "r") as f:
            return f.read()


###################################################################################################################
######## MCP tools go here ########################################################################################
###################################################################################################################


mcp = FastMCP(name="Git Course",
              instructions="This server provides an interactive course to help users learn Git version control.")

state = CourseState()


@mcp.tool
def clear_git_course_history() -> str:
    """
    Clears the course history and resets the course state.

    Returns:
        str: A message indicating that the course history has been cleared.
    """
    state.init_state()
    return "Your course history has been cleared. You can start over by using the 'start_course' tool."


@mcp.tool
def get_git_course_status() -> str:
    """
    Returns the current status of the Git course, including the current lesson and step.

    Returns:
        str: A message indicating the current lesson and step in the course.
    """
    current_lesson = state.state["current_lesson"]
    current_step = state.state["current_step"]
    lessons = state.state["lessons"]

    if current_lesson < len(lessons):
        lesson_name = lessons[current_lesson]["name"]
        step_name = lessons[current_lesson]["steps"][current_step]["name"]
        return f"You are currently on lesson '{lesson_name}', step '{step_name}'."
    else:
        return "You have completed all lessons in the course!"


@mcp.tool
def start_git_course() -> str:
    """
    Starts the Git course resumes the course from where the user left off, if there is no state, the course will start from the beginning.

    Returns:
        str: The introduction content for the Git course.
    """
    # TODO: this need to return the introduction content. We need to figure out if the course already started or not.
    return state.get_current_step_content()



@mcp.tool
def next_git_course_step(step_content: str, is_first_step: bool = False) -> str:
    """
    Moves to the next step in the Git course and returns the content for that step.

    Args:
        step_content (str): The content for the current step.
        is_first_step (bool): Whether this is the first step of the course.

    Returns:
        str: The content for the next step in the Git course.
    """
    return wrap_content_in_prompt(step_content, is_first_step)

@mcp.tool
def start_git_lesson_step(lesson_idx: int, step_index: int) -> str:
    """
    Sets the current lesson and step in the course state and returns the content for that step.
    Args:
        lesson_idx (int): The index of the lesson to set as current.
        step_index (int): The index of the step to set as current.
    Returns:
        str: The content for the current step in the course after setting the lesson and step.
    """
    try:
        state.set_current_lesson_step(lesson_idx, step_index, has_started=True)
        step_content = state.get_current_step_content()
        return wrapContentInPrompt(step_content, is_first_step=(lesson_idx == 0 and step_index == 0))
    except Error as e:
        raise ToolError(str(e))


def main():
    mcp.run()


if __name__ == "__main__":
    main()
