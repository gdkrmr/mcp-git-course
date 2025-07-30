# Adding a Remote and Pushing Your Local Repository

## Overview
In this lesson, you will learn how to connect your local Git repository to a remote server and push your project for the first time. This enables collaboration and backup on a remote platform.

## Step 1: Create a Remote Repository

1. Log in to your account on `git.sc.uni-leipzig.de`.
2. Create a new repository (for example, named `my-project`).
3. Copy the SSH URL for your new repository. It will look like:
   ```
   git@git.sc.uni-leipzig.de:your-username/my-project.git
   ```

## Step 2: Add the Remote to Your Local Repository

1. Open your terminal and navigate to your local project directory (initialized in the previous lesson).
2. Add the remote repository:
   ```bash
   git remote add origin git@git.sc.uni-leipzig.de:your-username/my-project.git
   ```
   Replace `your-username` and `my-project` with your actual username and repository name.

## Step 3: Push Your Local Repository to the Remote

1. Push your local commits to the remote repository:
   ```bash
   git push -u origin main
   ```
   - If your default branch is called `master`, use:
     ```bash
     git push -u origin master
     ```
2. The `-u` flag sets the remote `origin` as the default for future pushes and pulls.

## Step 4: Verify the Push

1. Go to your repository page on `git.sc.uni-leipzig.de`.
2. You should see your files and commit history.

## Conclusion
You have successfully connected your local repository to a remote server and pushed your project. You can now collaborate with others and keep your work backed up online.

## Additional Resources
- [Git Official Documentation: git remote](https://git-scm.com/docs/git-remote)
- [Git Official Documentation: git push](https://git-scm.com/docs/git-push)