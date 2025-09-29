# Merging Branches and Resolving Conflicts in Git

## Overview

In this lesson, you will learn how to merge branches in Git and resolve conflicts that may arise during the process. Merging is a fundamental part of collaborative workflows, allowing you to integrate changes from different branches into a unified codebase.

## Step 1: Understanding Merging

- **Merging** is the process of integrating changes from one branch into another. The most common scenario is merging a feature branch into the main branch after development is complete.

- **Fast-forward merge:** If the main branch has not changed since the feature branch was created, Git simply moves the branch pointer forward.

## Step 2: Preparing for a Merge

1. Ensure your working directory is clean:
   ```bash
   git status
   ```
2. Switch to the branch you want to merge into (usually `main` or `master`):
   ```bash
   git switch main
   ```
3. Pull the latest changes from the remote repository:
   ```bash
   git pull
   ```

## Step 3: Merging a Branch

1. Merge the feature branch into your current branch:
   ```bash
   git merge feature-branch
   ```
2. If there are no conflicts, Git will complete the merge and create a new merge commit.

## Step 4: Resolving Merge Conflicts

Sometimes, changes in both branches affect the same lines in a file, resulting in a conflict. Git will pause the merge and mark the conflicted files.

1. Identify conflicted files:
   ```bash
   git status
   ```
2. Open the conflicted files in your editor. Git marks conflicts like this:
   ```diff
   <<<<<<< HEAD
   Your changes in the current branch
   =======
   Changes from the branch being merged
   >>>>>>> feature-branch
   ```
3. Edit the file to resolve the conflict, keeping the desired changes.
4. After resolving all conflicts, add the resolved files:
   ```bash
   git add <filename>
   ```
5. Complete the merge:
   ```bash
   git commit
   ```
   - Git may auto-create a merge commit message. You can edit it if needed.

## Step 5: Best Practices for Merging

- Communicate with your team before merging large changes. Usually this is done through "Pull requests" and/or "Issues" on the code hosting platform (e.g. Github, Gitlab, ...)
- Pull the latest changes before starting a merge.
- Test your code after resolving conflicts.
- Use descriptive commit messages for merges.

## Conclusion

You have learned how to merge branches in Git and resolve conflicts. Merging is essential for integrating work from multiple contributors and maintaining a cohesive project history.

## Questions/Exercises
1. Do the [Guestbook exercise](https://git.sc.uni-leipzig.de/ws2025rdm/guestbook). Give the output of the merge conflict.
2. This is an example of a merge conflict. Resolve it and explain your reasoning.
   ```python
   <<<<<<< HEAD
   print(f"Today is {date.today()}")
   =======
   print(f"The time is {datetime.now().strftime('%H:%M:%S')}")
   >>>>>>> feature-return-time
   ```
3. Here is another example of a merge conflict. Resolve it and explain your reasoning.
   ```javascript
   <<<<<<< HEAD
   function calculateTotal(price, tax) {
       return price + (price * tax);
   }
   =======
   function calculateTotal(price, discount) {
       return price - discount;
   }
   >>>>>>> feature-discount
   ```

## Additional Resources

- [Git Official Documentation: git merge](https://git-scm.com/docs/git-merge)
- [Pro Git Book: Branches in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- [Atlassian: How to resolve merge conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)
