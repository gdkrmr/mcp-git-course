from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from rdm_mcp.state import CourseState
from rdm_mcp.prompts import wrap_content_in_prompt

# This should not be necessary the client should be able to run commands directly
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
    state.build_initial_state()
    state.save_state()
    return "Your course history has been cleared. You can start over by using the 'start_git_course' tool."


@mcp.tool
def get_git_course_status() -> str:
    """
    Returns the current status of the Git course, including the current lesson and step.

    Returns:
        str: A message indicating the current lesson and step in the course.
    """
    # return state.to_json()

    has_started = state.state["has_started"]
    current_lesson = state.state["current_lesson"]
    current_step = state.state["current_step"]
    lessons = state.state["lessons"]

    if not has_started:
        return "You have not started the Git course yet. Use the 'start_git_course' tool to begin."

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
    return wrap_content_in_prompt(state.get_current_step_content())


@mcp.tool
def next_git_course_step() -> str:
    """
    Moves to the next step in the Git course and returns the content for that step.

    Args:
        step_content (str): The content for the current step.
        is_first_step (bool): Whether this is the first step of the course.

    Returns:
        str: The content for the next step in the Git course.
    """
    return wrap_content_in_prompt(state.advance_step())


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
