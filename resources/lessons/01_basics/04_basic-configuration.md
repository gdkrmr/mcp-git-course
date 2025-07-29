# Basic Configuration

## Configure username and email

To function properly, git needs to know your name and email.

1. Configure your username:
   ```bash
   git config --global user.name "Your Name"
   ``` 

2. Configure your email:
   ```bash
   git config --global user.email "you@example.com"
   ``` 

## Verify Configuration

To check your configuration settings, run:
```bash
git config --global --list
``` 
You should see an output listing your configured username and email:
```
user.name=Your Name
user.email=you@example.com
``` 
