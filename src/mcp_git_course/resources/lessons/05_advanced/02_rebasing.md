# Rebasing Branches in Git

## Overview
Rebasing is a way to move or combine a sequence of commits to a new base commit. It helps keep your project history linear and up-to-date with the main branch.

## What is Rebasing?
Rebasing takes the changes from one branch and reapplies them on top of another branch. This is often used to update a feature branch with the latest changes from `main` before merging.

## Step 1: Prepare for Rebasing

1. Make sure your working directory is clean:
   ```bash
   git status
   ```
   You should see "nothing to commit, working tree clean".

## Step 2: Rebase Your Branch onto Main

1. Switch to your feature branch:
   ```bash
   git checkout feature-branch
   ```
2. Start the rebase:
   ```bash
   git rebase main
   ```
   This will replay your commits on top of the latest `main` branch.

## Step 3: Resolve Conflicts (if any)

1. If you see a conflict, Git will pause and mark the conflicted files.
2. Open the conflicted files, resolve the differences, then add the resolved files:
   ```bash
   git add <filename>
   ```
3. Continue the rebase:
   ```bash
   git rebase --continue
   ```
4. Repeat until the rebase is complete.

## Step 4: Verify the Rebase

1. Check your commit history:
   ```bash
   git log --oneline --graph
   ```
   Your feature branch commits should now appear on top of the latest `main` commits.

## Step 5: Push the Rebasing Result

1. If you have already pushed your branch before rebasing, you need to force-push:
   ```bash
   git push --force-with-lease
   ```
   This updates the remote branch with your rebased commits.

## Tasks for the Student

- Rebase your feature branch onto the latest `main` branch.
- Resolve any conflicts that occur during the rebase.
- Verify your commit history is linear and up-to-date.
- Push your rebased branch to the remote repository.

## Additional Resources

- [Git Official Documentation: git rebase](https://git-scm.com/docs/git-rebase)
- [Pro Git Book: Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)