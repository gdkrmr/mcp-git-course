# Creating and Verifying an SSH Key

## Overview
SSH keys provide a secure way to authenticate with remote Git repositories without using passwords. In this lesson, you will learn how to create an SSH key pair, add it to your Git hosting service, and verify the setup.

## Step 1: Generate an SSH Key Pair

1. Open your terminal.
2. Run the following command to generate a new SSH key pair:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   If your system does not support `ed25519`, use:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
3. When prompted, you can press Enter to accept the default file location.
4. Optionally, set a passphrase for added security.

## Step 2: Add Your SSH Key to the SSH Agent

1. Start the SSH agent:
   ```bash
   eval "$(ssh-agent -s)"
   ```
2. Add your SSH private key to the agent:
   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```
   - If you used RSA, the file will be `~/.ssh/id_rsa`.

## Step 3: Copy Your Public Key

1. Copy the contents of your public key to your clipboard:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
   - Select and copy the output.
   - NOTE: the file **without** the ~.pub~ ending is your private key, this key should **not** leave your machine.

## Step 4: Add the SSH Key to Your Git Hosting Service

- Go to your account settings on GitHub, GitLab, or Bitbucket.
- Find the section for SSH keys and add your copied public key.

## Step 5: Verify Your SSH Connection

Test your connection by running:
```bash
ssh -T git@github.com
ssh -T git.sc.uni-leipzig.de
```
- If successful, you will see a message like:
  `Hi $username! You've successfully authenticated.`

## Conclusion
You have now created and verified your SSH key. This allows you to securely interact with remote Git repositories using SSH authentication.

## Questions
1. An SSH key is a pair of cryptographic keys used for secure authentication. Why should your private key never leave your device?
2. Why does your key consist of two files? What are these files and what is their content?
3. What are the benefits of using SSH keys over HTTPS for Git operations?
4. SSH agents help you manage your SSH keys by keeping them in memory, so you don't have to enter your passphrase every time. How does this improve your workflow?
5. What is the best ssh agent for your use case? Ask the LLM for help if you are unsure.

## Additional Resources
- [GitHub: Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [GitLab: SSH Keys](https://docs.gitlab.com/ee/ssh/)
