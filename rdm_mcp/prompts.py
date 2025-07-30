INTRODUCTION_PROMPT = """
This is a course to help a new user learn about Git, the widely used version control system.
The following is the introduction content, please provide this text to the user EXACTLY as written below. Do not provide any other text or instructions:

# Welcome to the Git Course!

Thank you for registering for the Git course! This interactive guide will help you learn how to effectively use Git for version control.

## How This Course Works

- Each lesson is broken into multiple steps
- I'll guide you through common commands and workflows
- You can ask questions at any time
- If you ever leave and come back, use the `start_git_course` tool to pick up where you left off. Just ask to "start the Git course".
- Use the `next_git_course_step` tool to move to the next step when you're ready. Just ask to "move to the next step" when you are ready.
- Use the `get_git_course_status` tool to check your progress. You can just ask "get my course progress".
- Use the `clear_git_course_history` tool to reset your progress and start over. You can just ask "clear my course progress".

You can always ask for help or clarification on any topic. I'm here to assist you! Please ask any questions you have about the course or Git in general.

Type "start git course" and let's get started with your first lesson!
"""

LESSON_PROMPT = """This is a course to help a new user learn about Git, the widely used version control system.
Please help the user through the steps of the course by guiding them through the content and assisting them in writing the initial version of their Git commands. The goal is to demonstrate how the commands work and explain the concepts as the course progresses. Each lesson is divided into steps. You should return the content of each step and ask the user to move to the next step when they are ready. If a step includes instructions to execute commands, you should provide the commands for the user when applicable. Always briefly explain the step before presenting the commands. Please ensure to return any text in markdown blockquotes exactly as written in your response. This is important."""

COURSE_OVERVIEW = """

"""

def wrap_content_in_prompt(content: str) -> str:
    wrapped_content = f"""{LESSON_PROMPT}\n\nHere is the content for this step:\n\n <StepContent>\n{content}\n</StepContent>"""
    return f"""{wrapped_content}\n\nWhen you are ready to continue, use the 'next_git_course_step' tool to move to the next step."""
