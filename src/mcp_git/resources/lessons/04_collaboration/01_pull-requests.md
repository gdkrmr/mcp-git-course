# Collaboration Workflows in Git: Pull Requests with Hands-On Exercise

## Overview
Pull requests (PRs) are essential for collaborative development. They allow you to propose changes, initiate code reviews, and merge contributions seamlessly into the main branch. In this lesson, you'll learn the process of working with pull requests and put your skills to the test with a hands-on exercise.

## What is a Pull Request?
A pull request is a request to merge changes from one branch (typically a feature branch) into another branch (usually `main` or `master`). PRs give your team an opportunity to review your code, suggest improvements, and ensure that the changes fit the project’s standards before merging.

## Making a Pull Request

Take the typo you fixed in the previous exercise and create a pull request to merge it into the main branch.

1. **Push Your Changes**: Ensure your changes are committed and pushed to your feature branch.
   ```bash
   git push origin $USER/typo-fix
   ```
2. **Open a Pull Request**:
    - Go to your repository on Gitlab.
    - Click on the "Merge Requests" tab.
    - Click on "New Merge Request".
    - Select your feature branch as the source and `main` as the target.
    - Fill in the title and description of your pull request, explaining the changes you made.

3. **Submit the Pull Request**: Click on "Create Merge Request" to submit your PR.
4. **Review and Respond**:
    - Reviewers will comment on your PR. Address their feedback by making additional commits to your branch.
    - Once all feedback is addressed, you can merge the PR if you have the necessary permissions.

5. **Merge the Pull Request**:
    - If you have permission, click on "Merge" to integrate your changes into the main

## Questions
1. What is the purpose of a pull request in collaborative development? How is it different from a regular merge?
2. How can you address feedback from reviewers in a pull request?
