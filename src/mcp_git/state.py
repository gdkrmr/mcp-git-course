import os
import json
from mcp_git.prompts import INTRODUCTION_PROMPT
from mcp_git.config import STATE_DIR, COURSE_DIR
from fastmcp.exceptions import ToolError


class CourseState():
    """
    Manages the state of the Git course, including current lesson and step.
    This class is responsible for initializing, loading, saving, and advancing the course state.
    It reads the course directory to build the initial state and provides methods to advance steps and retrieve content.

    Attributes:
        state (dict): The current state of the course, including current lesson and step.

    Methods:
        set_current_lesson_step(lesson_idx: int, step_index: int, has_started: bool) -> None:
            Sets the current lesson and step in the course state.
        build_initial_state() -> None:
            Reads the course directory and builds the initial state for the course.
        load_state() -> None:
            Loads the course state from the state directory.
        save_state() -> None:
            Saves the current state of the course to the state directory.
        advance_step() -> str:
            Advances to the next step in the course and returns its content.
        get_current_step_content() -> str:
            Returns the content of the current step in the course.
    """

    def __init__(self):
        if os.path.exists(os.path.join(STATE_DIR, "state.json")):
            self.load_state()
        else:
            self.build_initial_state()
            self.save_state()


    def set_current_lesson_step(self, lesson_idx: int, step_index: int, has_started: bool) -> None:
        """
        Sets the current lesson and step in the course state.

        Args:
            lesson_idx (int): The index of the lesson to set as current.
            step_index (int): The index of the step to set as current.
        """
        if lesson_idx < 0 or step_index < 0:
            raise ToolError("Lesson index and step index must be non-negative integers.")

        if lesson_idx >= len(self.state["lessons"]):
            raise ToolError(f"Lesson index {lesson_idx} is out of range. There are only {len(self.state['lessons'])} lessons.")

        if step_index >= len(self.state["lessons"][lesson_idx]["steps"]):
            raise ToolError(f"Step index {step_index} is out of range for lesson {lesson_idx}. It has only {len(self.state['lessons'][lesson_idx]['steps'])} steps.")

        self.state["current_lesson"] = lesson_idx
        self.state["current_step"] = step_index
        self.state["has_started"] = has_started
        self.save_state()


    def build_initial_state(self) -> None:
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

        self.state = {
            "current_lesson": 0,
            "current_step": 0,
            "has_started": False,
            "lessons": lessons
        }


    def load_state(self) -> None:
        """
        Loads the course state from the state directory.

        Returns:
            dict: The current state of the course.
        """
        state_file = os.path.join(STATE_DIR, "state.json")
        if not os.path.exists(state_file):
            raise ToolError(f"State file '{state_file}' does not exist. Please initialize the state first.")

        with open(state_file, "r") as f:
            self.state = json.load(f)


    def save_state(self) -> None:
        """
        Saves the current state of the course to the state directory.
        """
        if not os.path.exists(STATE_DIR):
            os.makedirs(STATE_DIR)
        state_file = os.path.join(STATE_DIR, "state.json")
        with open(state_file, "w") as f:
            json.dump(self.state, f, indent=4)


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

        self.save_state()
        return self.get_current_step_content()


    def get_current_step_content(self) -> str:
        """
        Returns the content of the current step in the course.

        Returns:
            str: The content of the current step.
        """
        if not self.state["has_started"]:
            return f"self.state['has_starte']: {self.state['has_started']}, {INTRODUCTION_PROMPT}"

        current_lesson = self.state["current_lesson"]
        current_step = self.state["current_step"]

        lesson = self.state["lessons"][current_lesson]
        step = lesson["steps"][current_step]

        step_path = os.path.join(COURSE_DIR, lesson["direcory"], step["file"])
        if os.path.exists(step_path):
            with open(step_path, "r") as f:
                return f.read()
        raise ToolError("Step content not found.")

    def to_json(self) -> str:
        """
        Returns the current state of the course as a JSON string.

        Returns:
            str: The current state of the course in JSON format.
        """
        return json.dumps(self.state, indent=4)
