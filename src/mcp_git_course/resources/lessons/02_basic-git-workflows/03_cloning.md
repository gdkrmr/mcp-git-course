# Cloning a Remote Git Repository

## Overview
In this lesson, you will learn how to clone a remote Git repository to your local machine. Cloning is the process of creating a local copy of a repository that exists on a remote server. This allows you to work on the project, track changes, and collaborate with others.

## Step 1: Obtain the Repository URL

To clone a repository, you need its URL. For this lesson, we will use the following repository:
```
git@git.sc.uni-leipzig.de/ws2025rdm/materials
```

## Step 2: Clone the Repository

1. Open your terminal.
2. Navigate to the directory where you want to store the cloned repository.
3. Run the following command:
   ```bash
   git clone git@github.com:gdkrmr/git-mcp-course-example.git example
   ```
4. This command will create a new directory named `example` containing all the files and history from the remote repository.

## Step 3: Verify the Clone

1. Change into the newly created directory:
   ```bash
   cd materials
   ```
2. Check the repository status:
   ```bash
   git status
   ```
3. List the files:
   ```bash
   ls -la
   ```
4. You should see the project files and be able to use all Git commands as usual.

## Step 4: Work with the Cloned Repository

- You can now edit files, stage changes, commit, and push updates to the remote repository.
- To fetch new changes from the remote repository:
  ```bash
  git pull
  ```
- To push your changes to the remote repository:
  ```bash
  git push
  ```

## Conclusion
You have successfully cloned a remote Git repository to your local machine. You are now ready to collaborate and contribute to the project.

## Questions
1. explain the different parts of the command `git clone git@github.com:gdkrmr/git-mcp-course-example.git example`, which one(s) are optional?
2. What files and directories were created when you cloned the repository?
3. What is the secret from the repository?
4. What is the license?
5. How can you check the remote repository URL of your cloned repository?
6. What is the difference between `git` and `Gitlab` or `GitHub`?




## Additional Resources
- [Git Official Documentation: git clone](https://git-scm.com/docs/git-clone)
- [Pro Git Book: Cloning a Repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
