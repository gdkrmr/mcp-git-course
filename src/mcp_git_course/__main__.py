from fastmcp import FastMCP  # , Context
from fastmcp.exceptions import ToolError
from mcp_git_course.state import CourseState
from mcp_git_course.prompts import wrap_content_in_prompt
from typing import Any


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


MCP: FastMCP[None] = FastMCP(
    name="Git Course",
    instructions="This server provides an interactive course to help users learn Git version control.",
)

STATE: CourseState = CourseState()


@MCP.tool
def clear_git_course_state() -> str:
    """
    Clears the course history and resets the course state.

    Returns:
        str: A message indicating that the course history has been cleared.
    """
    STATE.reset_state()
    return "Your course history has been cleared. You can start over by using the 'start_git_course' tool."


@MCP.tool
def get_git_course_status() -> str:
    """
    Returns the current status of the Git course, including the current lesson and step.

    Returns:
        str: A message indicating the current lesson and step in the course.
    """
    # return state.to_json()

    current_lesson = STATE.state["current_lesson"]
    current_step = STATE.state["current_step"]
    lessons = STATE.state["lessons"]

    if current_lesson < len(lessons):
        lesson_name = lessons[current_lesson]["name"]
        step_name = lessons[current_lesson]["steps"][current_step]["name"]
        return f"You are currently on lesson '{lesson_name}', step '{step_name}'."
    else:
        return "You have completed all lessons in the course!"


@MCP.tool
def start_git_course() -> str:
    """
    Starts the Git course resumes the course from where the user left off, if there is no state, the course will start from the beginning.

    Returns:
        str: The introduction content for the Git course.
    """
    return wrap_content_in_prompt(STATE.get_current_step_content())


@MCP.tool
async def next_git_course_step(questions_answered: bool, insists: bool) -> str:
    """
    Moves to the next step in the Git course and returns the content for that step or tells the user to answer the questions or complete the exercises before moving on.

    Args:
        questions_answered (bool): Indicates whether the user has provided correct answers to the questions in the current step in a prompt. If the answers are not correct, the user should be prompted to answer the questions again.

        insists (bool): Indicates whether the user insists on moving to the next step regardless of whether they have answered the questions. Insisting means that the user explicitly mentions the word "insist" in the current prompt.

    Returns:
        str: The content for the next step in the Git course or a message prompting the user to answer the questions or complete the exercises before moving on.
    """

    if questions_answered or insists:
        return wrap_content_in_prompt(STATE.advance_step())
    else:
        return "Please answer the questions or complete the exercises before moving to the next step. If you want to move to the next step anyway, please insist on it."

    ### I don't think any client supports sampling yet, so this is commented out for now. I have implemented the logic in the description of the parameters of the tool.

    # prompt = """Check the following and answer in a single word:
    #    - Are there any questions in the current step? If there are no question answer "noquestions".
    #    - Did the user anser the questions in the current step? Answer 'yes'.
    #    - Did the user insist on advancing to the next step? Answer 'insist'.
    #    """

    # ctx_response = await ctx.sample(prompt)
    # response = ctx_response.text.strip().lower()

    # if "yes" in response:
    #    return wrap_content_in_prompt(state.advance_step())
    # elif "noquestion" in response:
    #    return wrap_content_in_prompt(state.advance_step())
    # elif "insist" in response:
    #    return wrap_content_in_prompt(state.advance_step())
    # else:
    #    return "Please answer the questions or complete the exercises before moving to the next step. If you want to move to the next step anyway, please insist on it."


@MCP.tool
def start_git_lesson_step(lesson_idx: int, step_index: int) -> str:
    """
    Sets the current lesson and step in the course state and returns the content for that step. Do not use this tool to advance the course, use `next_git_course_step` instead.

    Args:
        lesson_idx (int): The index of the lesson to set as current.
        step_index (int): The index of the step to set as current.
    Returns:
        str: The content for the current step in the course after setting the lesson and step.
    """
    try:
        STATE.set_current_lesson_step(lesson_idx, step_index)
        step_content = STATE.get_current_step_content()
        return wrap_content_in_prompt(step_content)
    except Exception as e:
        raise ToolError(str(e))


def main():
    MCP.run()


if __name__ == "__main__":
    main()
