## Linux Commands:
```python
cd #Change directory
ls
ls -la
rm -rf <folderName>
touch <fileName>
vi <fileName> #after vi, press "i" to insert the contents and to save press "esc" :wq (write and quit)
cat <fileName>
```

### Check version:
```python
git --version
```

### Set config values:
```python
git config --global user.name "Naren"
git config --global user.email "narendas10@gmail.com"
git config --list
```

### Need Help?
```python
git help config(verb)
git <verb> --help
git help --all  # Show all git possible commands.
```

### Initialize Repo from existing code:
```python
git init
```

### Add .gitignore file:
```python
.DS_Store
.project
*.pyc
```

### Add files to Staging area:
```python
git add <fileName>
git add .  # "." denotes current directory.
git add -A  # "-A" denotes all files in local repo and sub-repo.
git add --all
git add --no-all  # It includes created(new), modified files, but excludes deleted files.
git add -u  # "-u" denotes update.
git add --update  # It includes modified, deleted files, but excludes created files.
git status
```

### Remove files from staging area:
```python
git reset <fileName>
git status
git rm --cached <fileName>  # "rm" denotes remove.
git restore --staged <filename>
```

### Initial Commit:
```python
git add -A
git commit -m "First Commit"  # "-m" denotes message.
git status
git log
```

### To rename the commit message:
```python
git commit --amend -m "Completed"
git commit -a -m "Completed"

git commit --amend  # Can modify or add files to the previous commit but not in same ID.
git log --stat  # To display the detailed log report.
git log -p -3 # To display last 3 commits.
```

### Cloning a remote Repo:
```python
git clone <url> <where to clone>
git clone ../remote_repo.git .
```

### About remote Repo:
```python
git remote -v  # Shows remote origins(Repo Name).
git branch -a  # Shows all local and remote branches.
```

### Checking Difference and Push to remote:
```python
git diff
git status 
git add -A
git commit -m "Modified function"

git diff <1.commit ID> <2.commit ID>  # Shows the difference between two commits.
```

### Push and Pull on Remote:
```python
git remote add origin https://github.com/NarenBot/demo.git
git remote add ssh-origin https://github.com/NarenBot/demo.git  # Using SSH.
git branch -M main # To rename the current branch-name to 'main'

git pull origin main
git pull origin main --allow-unrelated-histories  #If error on unrelated histories

git push -u origin main  # "u" denotes upload and origin means remote-Repo name.
git push -f origin main  # It overrides the remote branch code with your local repo code.
```

### After renaming the 'master' branch-name to 'main'
```python
git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
```

### Creating Branch:
```python
git branch <branchName>
git checkout <branchName>  # To navigate use "checkout"
git checkout -b <branchName> # Create, and move to a new branch.
```

#### Some of Advance Questions:
01. pull is a combination of?  fetch and then merge.
02. Merge the current branch with the branch main, on origin?  git merge origin/main
03. Update the current branch from its origin?  git pull origin
04. List all local and remote branches?  git branch -a
05. List only remote branches?  git branch -r
06. Rename the origin?  git remote rename origin oldname newname
07. In .gitignore add a line to ignore all .temp files?  *.temp
08. In .gitignore add a line to ignore all files in any directory named temp?  temp/
09. In .gitignore add a single line to ignore all files named temp1.log, temp2.log?  temp?.log
10. In .gitignore, ignore all .log files, except main.log?  *.log !main.log
11. Show the log of the repository, showing just 1 line per commit?  git log --oneline
12. revert the latest commit?  git revert HEAD
13. revert the latest commit, skipping the commit message editor?  git revert HEAD --no-edit
14. revert the two last commits?  git revert HEAD~1
15. reset to the commit with the hash abc1234?  git reset abc1234    


### Merge a Branch:
```python
git checkout master
git pull origin master
git branch --merged
git merge <branchName>
git push origin master
```

### Deleting a Branch:
```python
git branch --merged
git branch -d <branchName>  # "d" denotes delete.
git branch -a 
git push origin --delete <branchName>
```

### To move the commit ID from one branch to another: [cherry-pick]
```python
git log  --> # Should copy the commit ID for moving another branch.
git branch <branchName>
git checkout <branchName>
git cherry-pick <commit ID>
git checkout <master> 
```

### Types of resets: soft, mixed and hard.
```python
git reset --soft <initial commit ID>  # This will remove all commits except initial one with next staging area.
git reset --hard <initial commit ID>  # This will remove all commits except initial one with previous staging area.
```

### To clean untracked files:
```python
git clean -df # "d" denotes directory and "f" denotes files.
```

### To show the complete history:
```python
git reflog
git revert <commit ID>  # It creates a new commit and revert the changes of previous commit.
```

### Stashing:
```python
git branch <branchName>
git stash save "message"    # It will undo the process inside any changes on files.
git stash apply <stash ID>  # It will redo the process inside any changes on files.
git stash list
git checkout -- .  # undo process
git stash pop      # redo process and also deletes the stash ID.

git stash clear
git stash drop <stash ID>
```

```python
git config --global --list  # To check whether diffmerge is added or not as "difftool".
```

### To change the branch-name from master to main in VS Code.
```python
git branch --set-upstream-to=origin/main main
```

- To download diffmerge: http://www.sourcegear.com/products.html
- To setup with Git, add .gitconfig file inside C:\Users\Naren ...... http://www.sourcegear.com/diffmerge/webhelp/chapter_integration.html