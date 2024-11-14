# Git Bash Commands
### Navigating The Terminal
**ls** (list files/directories)
**cd <name>** (change directory to the name identified)
**cd ..** (or) **cd -** (To go to the previous directory) 
**cd ~/<directory1>/<directory2>/...** (to change directory to a directory starting at the Users/<name> directory)
**pwd** (print working directory)

### Git Basics 
#### Change to the appropriate local directory 
**git init** (Initialize a local git project, be within the folder you wish to create into a git repository)
**git status** (Displays the state of the working directory and the staging area; i.e. unstaged or staged files)
**git add <filename.extension>** (or) **.** (or) **<folder/>** (or) **<folder/.../<filename.extension>** (Add a file to the staging area either by filename or with the period to add all untracked files to the staging area)
**git restore --staged <filename.extension>** (To remove a file from the staging area)
**git rm --cached <folder/.../<filename.extension>** (To remove a file within a folder from the staging area)
**git rm --cached -r <folder/>** (To remove a folders entire contents from the staging area)
**git commit -m "enter commit message here"** (All tracked files will  now be commited into a snapshot of the project at that specific time and given a hash for tracking purposes)
**git commit -a -m "Enter message"** (commits all changes but bypasses the staging area)
