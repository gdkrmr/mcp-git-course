# Stashing Changes in Git

## Overview
Stashing allows you to temporarily save changes in your working directory that are not yet ready to be committed. This is useful if you need to quickly switch branches or work on something else without losing your current work.

## Task 1: Create a Stash

1. Make changes to a file in your repository (e.g., edit `README.md`).
2. Save your changes to a stash:
   ```bash
   git stash
   ```
3. Verify that your working directory is clean:
   ```bash
   git status
   ```
   You should see "nothing to commit, working tree clean".

## Task 2: List Stashes

1. List all stashes you have created:
   ```bash
   git stash list
   ```
   You should see a list of stashes, e.g., `stash@{0}: WIP on main: ...`.

## Task 3: Apply a Stash

1. Apply the most recent stash to your working directory:
   ```bash
   git stash apply
   ```
2. Verify that your changes have been restored:
   ```bash
   git status
   ```
   You should see your previously stashed changes as modified files.

## Task 4: Drop or Pop a Stash

1. Remove the most recent stash after applying it:
   ```bash
   git stash drop
   ```
   Or apply and remove in one step:
   ```bash
   git stash pop
   ```
2. Verify that the stash has been removed:
   ```bash
   git stash list
   ```
   The stash should no longer appear in the list.

## Conclusion

You have learned how to stash changes, list stashes, apply them, and remove them. Stashing is a valuable tool for managing work in progress and switching contexts efficiently.

## Questions/Exercises

1. Take one of your repositories and edit a file. What is the output of `git status`?
2. Stash the change. What is the output of `git status`?
3. Pop the stash. What is the output of `git status`?

## Additional Resources
- [Git Official Documentation: git stash](https://git-scm.com/docs/git-stash)
- [Pro Git Book: Stashing and Cleaning](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning)
