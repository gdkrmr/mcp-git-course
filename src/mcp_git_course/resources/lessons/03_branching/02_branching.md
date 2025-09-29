# Branching in Git

## Overview

Branching is a powerful feature in Git that allows you to diverge from the main line of development and work on new features, bug fixes, or experiments in isolation. This lesson covers what branches are, how to create and switch between them, and why they are essential for collaborative development.

## What is a Branch?

A branch in Git is simply a pointer to a specific commit in your repository’s history. The default branch is usually called `main` or `master`. By creating branches, you can work independently on different tasks without affecting the main codebase.

## 1: Viewing Existing Branches

To see all branches in your repository, use:
```bash
git branch
```
- The current branch will be highlighted with an asterisk (`*`).

To see all branches, including remote branches:
```bash
git branch -a
```

## 2: Creating a New Branch

To create a new branch, use:

```bash
git branch <branch-name>
```

For example, to create a branch called `feature-x`:
```bash
git branch feature-x
```

## 3: Switching Between Branches

To switch to another branch, use:

```bash
git switch <branch-name>
```

For example:

```bash
git switch feature-x
```

## 4: Creating and Switching in One Command

You can create and switch to a new branch in one step:
```bash
git checkout -b <branch-name>
```
Or:
```bash
git switch -c <branch-name>
```
For example:
```bash
git switch -c bugfix-123
```

## 5: Understanding Branch Use Cases

- **Feature Development:** Create a branch for each new feature.
- **Bug Fixes:** Use branches to isolate bug fixes.
- **Experimentation:** Try new ideas without affecting the main codebase.
- **Collaboration:** Team members can work on separate branches and merge their changes when ready.

## 6: Deleting a Branch

Once a branch is no longer needed, you can delete it:
```bash
git branch -d <branch-name>
```
If the branch hasn’t been merged, use:
```bash
git branch -D <branch-name>
```

## Best Practices

- Use descriptive names for branches (e.g., `feature/login-page`, `bugfix/issue-42`, `<initials>/fixtypo`).
- Regularly merge (see next lession) changes from the main branch to keep your branch up to date.
- Delete branches that are no longer needed to keep your repository clean.

## Conclusion

Branching in Git enables flexible, organized, and collaborative development. By mastering branches, you can manage multiple streams of work efficiently and safely.

## Questions
1. What is the purpose of creating branches in Git?
2. Find a typo in the materials repo. For this
   - Create a branch, 
   - Switch to the branch
   - Edit the file to make the fix,
   - push to the remote repository.

## Note

In the next step we will learn how to merge the changes into another branch.

## Additional Resources

- [Git Official Documentation: Branches](https://git-scm.com/docs/git-branch)
- [Pro Git Book: Branches in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
