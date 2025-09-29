# Tagging Commits in Git

## Overview
Tags in Git are used to mark specific points in your repository’s history, such as releases or milestones. Tags make it easy to reference important commits and share stable versions of your project.

## 1. Create a Lightweight Tag

1. In your project directory, create a tag for the current commit:
   ```bash
   git tag v1.0
   ```
2. Verify the tag was created:
   ```bash
   git tag
   ```
   You should see `v1.0` listed.

## 2. Create an Annotated Tag

1. Create an annotated tag with a message:
   ```bash
   git tag -a v1.1 -m "Release version 1.1"
   ```
2. View details of the annotated tag:
   ```bash
   git show v1.1
   ```

## 3. Tag a Specific Commit

1. Find the commit hash you want to tag:
   ```bash
   git log --oneline
   ```
2. Tag that commit:
   ```bash
   git tag v1.2 <commit-hash>
   ```

## 4. Push Tags to Remote

1. Push a single tag to the remote repository:
   ```bash
   git push origin v1.0
   ```
2. Push all tags:
   ```bash
   git push --tags
   ```
3. Verify tags on the remote platform (e.g., GitHub, GitLab).

## 5. List and Delete Tags

1. List all tags:
   ```bash
   git tag
   ```
2. Delete a local tag:
   ```bash
   git tag -d v1.0
   ```
3. Delete a remote tag:
   ```bash
   git push origin --delete v1.0
   ```

## Conclusion

Tags are essential for marking releases and important milestones in your project. Practice creating, viewing, and pushing tags to ensure you can manage project versions effectively.

## Additional Resources

- [Git Official Documentation: git tag](https://git-scm.com/docs/git-tag)
- [Pro Git Book: Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
