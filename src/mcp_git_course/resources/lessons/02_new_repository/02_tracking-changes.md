# Tracking Changes in Git

## Overview

In this lesson, you will learn how to track changes in your project using Git. Tracking changes is essential for monitoring modifications, preparing files for commits, and maintaining a clear history of your work.

## Step 1: Check the Status of Your Repository

1. Open your terminal and navigate to your project directory.
2. Run the following command to see the current state of your repository:
   ```bash
   git status
   ```
3. This command shows which files have been modified, added, or deleted, and which files are staged for commit.


## Step 2: Create a File

1. Create a file. You can do this with your text editor or with a command

   ```bash
   echo 'Hello, World!' > README.md
   ```

2. Run `git status`.

## Step 3: Stage a change

1. To prepare files for committing, add them to the staging area using:

   ```bash
   git add README.md
   ```

2. Run `git status` again to verify that your changes are staged.

### What is the Staging Area?

The staging area (also called the "index") is a space where you can collect changes you want to include in your next commit. When you use `git add`, you move changes from your working directory to the staging area. This lets you review and organize your changes before saving them permanently in the repository. Only files in the staging area will be included in your next commit.

## Step 4: Commit Changes

1. Once your changes are staged, commit them to the repository:

   ```bash
   git commit -m "Describe your changes here"
   ```

2. The commit message should clearly describe what was changed.

3. Run `git status`, it should say that there is nothing to commit and that the working tree is clean.

### What is a Commit?

- A commit is a snapshot of your project at a specific point in time. 
- When you commit, Git saves the changes that were staged, along with a message describing those changes. 
- Each commit has a unique identifier (hash) and records information about the author and date. 
- Commits link to previous commits forming the history of your project, allowing you to track progress and revert to previous states if needed.

## Step 5: View Commit History

1. To see a log of all commits in your repository, run:
   ```bash
   git log
   ```
2. This command displays each commit's hash, author, date, and message.

## Step 6: Unstage and Discard Changes (Optional)

- To unstage a file:
  ```bash
  git reset <filename>
  ```
- To discard changes in a file and revert to the last committed version:
  ```bash
  git checkout -- <filename>
  ```

## Conclusion

You have learned how to track changes in your project using Git. By checking status, staging files, committing changes, and viewing history, you can effectively manage your project's evolution.

## Questions

1. Provide the outputs of running git status and explain:
   1. output of `git status` for step 1
   2. output of `git status` for step 2
   3. output of `git status` for step 3
   4. output of `git status` for step 4
2. What is the purpose of the staging area in Git?
3. Here are two commit messages. Which one is more descriptive and why?
   - "Fixed bug"
   - "Fixed bug in user authentication that caused login failures for new users"
4. Why should commits be small and focused on a single change?
5. Practical
    - Create a file named `REAMDE.md` and add some text.
    - stage the file and commit it to the repository.
    - What is the output of `git log`?
    - What is the output of `git diff HEAD..HEAD~`

## Additional Resources

- [Git Official Documentation: git status](https://git-scm.com/docs/git-status)
- [Pro Git Book: Recording Changes to the Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

