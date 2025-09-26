# Initializing a Git Repository

## Overview
In this lesson, you will learn how to create a new Git repository on your local machine. Initializing a repository is the first step in tracking changes to your project with Git. We will reuse this directory during this lesson.

## Step 1: Choose or Create a Project Directory

1. Open your terminal.
2. Navigate to the directory where you want to create your project, or create a new directory:
   ```bash
   mkdir my-project
   cd my-project
   ```

## Step 2: Initialize the Repository

1. Run the following command to initialize a new Git repository:
   ```bash
   git init
   ```
2. This command creates a hidden `.git` directory in your project folder. `git` will use this directory to store all version control information.

## Step 3: Verify Initialization

1. To confirm that your repository has been initialized, run:
   ```bash
   git status
   ```
2. You should see a message indicating you are on the `main` (or `master`) branch and that there are no commits yet.

## Conclusion
You have successfully initialized a Git repository and made your first commit. You are now ready to start tracking changes and collaborating using Git.

## Questions
1. Look at your folder. What new files and folders do you see?


## Additional Resources
- [Git Official Documentation: git init](https://git-scm.com/docs/git-init)
- [Pro Git Book: Getting Started](https://git-scm.com/book/en/v2)
