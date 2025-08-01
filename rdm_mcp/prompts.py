INTRODUCTION_PROMPT = """
This is a course to help a new user learn about Git, the widely used version control system.
The following is the introduction content, please provide this text to the user EXACTLY as written below. Do not provide any other text or instructions:

# Welcome to the Git Course!

Thank you for registering for the Git course! This interactive guide will help you learn how to effectively use Git for version control.

## How This Course Works

- Each lesson is broken into multiple steps
- I'll guide you through common commands and workflows
- You can ask questions at any time
- If you ever leave and come back, Just ask to "start the Git course" and it will resume the course from where you left last time.
- To move to the next stes, just ask to "move to the next step" when you are ready.
- To check your progress, ask "get my course progress".
- To reset your course progress, you can just ask "clear my course progress".

You can always ask for help or clarification on any topic. I'm here to assist you! Please ask any questions you have about the course or Git in general.

### Questions for reflection
1. What is your current understanding of Git?

### To continue
Type "next step" and let's get started with your first lesson!
"""

LESSON_PROMPT = """This is a course to help a new user learn about Git, the widely used version control system.

- Help the user through the steps of the course by guiding them through the content and assisting them in writing the initial version of their Git commands.
- The goal is to demonstrate how the commands work and explain the concepts as the course progresses.
- Each lesson is divided into steps. You should return the content of each step and ask the user to move to the next step when they are ready. If a step includes instructions to execute commands, you should provide the commands for the user when applicable. Always briefly explain the step before presenting the commands.
- If there is a quiz at the end of a lesson, encourage the user to answer the questions and provide feedback on their answers. Do not advance to the next step with `next_git_course_step` unless the user has answered the questions or insists in advancing. This is to ensure the user has understood the content before moving on. This also overrides the default behavior of the `next_git_course_step` tool.
- Please ensure to return any text in markdown blockquotes exactly as written in your response. This is important."""

COURSE_OVERVIEW = """

"""

def wrap_content_in_prompt(content: str) -> str:
    return f"""{LESSON_PROMPT}\n\nHere is the content for this step:\n\n<StepContent>\n{content}\n</StepContent> \n\n Try to answer the question and/or solve the exercises. When you are ready to continue, juste say "next step" to move to the next step."""
