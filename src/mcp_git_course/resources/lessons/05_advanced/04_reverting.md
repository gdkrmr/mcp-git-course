*Lesson 05: Advanced, Step 04: Reverting*
# Reverting Commits in Git

## Overview
Reverting allows you to undo changes made by previous commits without rewriting history. This is useful for correcting mistakes or removing unwanted changes in a safe and traceable way.

## 1: Identify the Commit to Revert

1. Open your terminal and navigate to your repository.
2. View the commit history:
   ```bash
   git log --oneline
   ```
3. Find the hash of the commit you want to revert (e.g., `a1b2c3d`).

## 2: Revert the Commit

1. Run the revert command:
   ```bash
   git revert a1b2c3d
   ```
   - Replace `a1b2c3d` with the actual commit hash.
2. Git will create a new commit that undoes the changes from the specified commit.
3. If prompted, edit the commit message to explain why you are reverting.

## 3: Verify the Revert

1. Check your commit history again:
   ```bash
   git log --oneline
   ```
2. Confirm that a new commit with the message "Revert ..." appears.

## 4: Push the Revert to the Remote Repository

1. Push your changes:
   ```bash
   git push
   ```
2. Verify on your remote platform (e.g., GitHub, GitLab) that the revert commit is present.

## Notes

- If you need to revert multiple commits, repeat the process for each commit.
- If the commit to revert affects files that have been changed since, you may need to resolve conflicts.

## Additional Resources

- [Git Official Documentation: git revert](https://git-scm.com/docs/git-revert)
- [Pro Git Book: Undoing Things](https://git-scm.com/book/en/v2/Git-Tools-Resetting-Cleaning-and-Rewriting-History)