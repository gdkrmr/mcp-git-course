# Ignoring Files with .gitignore

## Overview
Some files in your project should not be tracked by Git, such as build artifacts, temporary files, or sensitive information. The `.gitignore` file tells Git which files and directories to ignore.

## Task 1: Create a .gitignore File

1. In your project directory, create a file named `.gitignore`.
2. Add the following lines to ignore Python bytecode and environment files:
   ```
   __pycache__/
   *.pyc
   .env
   ```
3. Save the file.

## Task 2: Verify .gitignore is Working

1. Create a file named `test.pyc` and a directory named `__pycache__` in your project.
2. Run:
   ```
   git status
   ```
3. Confirm that `test.pyc` and `__pycache__/` do NOT appear in the list of untracked files.

## Task 3: Add .gitignore to the Repository

1. Stage and commit your `.gitignore` file:
   ```
   git add .gitignore
   git commit -m "Add .gitignore to ignore unnecessary files"
   ```

## Additional Resources

- [gitignore.io](https://www.toptal.com/developers/gitignore) — Generate `.gitignore` templates for different languages and frameworks.
- [GitHub: Ignoring files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)
