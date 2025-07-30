# Installing Git

## Overview
In this lesson, we will walk through the steps to install Git on your system, verify that it is installed correctly, and set up your basic configuration.

## Step 1: Installing Git

### Windows
1. Download the Git installer from the official site: [Git for Windows](https://gitforwindows.org/).
2. Run the installer and follow the setup instructions, selecting your preferred options.

### macOS
1. Open Terminal.
2. Install Git via Homebrew by running:
   ```bash
   brew install git
   ``` 
   Alternatively, you can download the installer from [Git for macOS](https://git-scm.com/download/mac).

### Linux
1. Open a terminal.
2. Use your package manager to install Git. For example, on Debian/Ubuntu:
   ```bash
   sudo apt update
   sudo apt install git
   ``` 

## Step 2: Verifying Git Installation

After installation, you can verify that Git is installed correctly by opening a terminal and running:
```bash
git --version
``` 
This command should return the version of Git installed, confirming a successful installation. For example:
```
git version 2.34.1
``` 

## Step 3: Basic Configuration

1. Configure your username:
   ```bash
   git config --global user.name "Your Name"
   ``` 

2. Configure your email:
   ```bash
   git config --global user.email "you@example.com"
   ``` 

### Step 4: Verify Configuration

To check your configuration settings, run:
```bash
git config --global --list
``` 
You should see an output listing your configured username and email:
```
user.name=Your Name
user.email=you@example.com
``` 

## Conclusion
You have successfully installed Git and configured it with your user information. You can now proceed to the next lesson where we will discuss how to create a Git repository.

