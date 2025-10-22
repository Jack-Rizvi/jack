# 3.1 Vocabulary Review
# Git vs GitHub: Git is a DVCS stored on your computer and GitHub is an online web-based hosting service.
# Terminal vs. Command Line: The terminal is an application which lets you interact with the command line, the command line is a text interface which allows the user to issue commands to the computer.
# Local vs. Remote Repository: Local is stored on the computer, remote is stored elsewhere (server/other computer)
# Version Control: Is a systm for tracking and managing changes to files over time, often by comparing previous versions of the same file.
# Staging Area: An area in Git where files are prepared to be committed
# git add: Adds a file to the staging area from the working directory
# git commit: Records the staged changes into the local repository
# git push: Uploads the local commits to a remote repository
# git status: Displays the state of the working directory
# git pull: Fetches changes from a remote repository and downloads them to your computer
# pwd: prints working directory
# ls: lists contents of working directory
# cd: changes the working directory
# nano: allows you to edit files within the terminal
# touch: creates a new file from the terminal
# mv: moves files/directories around
# rm: removes files/directories
# cat: combines files together

# 3.2 Directory Tree
# pwd
# ls
# git pull brianna_repo / git pull origin main
# mv homework.py homework/
# cd brianna_repo
# nano homework.py
# git add homework.py, git commit -m "Message", git push origin main
# You need to pull from the remote repository first before pushing.
# ~/Recent/

# 4.1 Data Types
def checkDataTypes(input):
    output = str(type(input))
    range = (len(output)-1)
    return output[6:range]
print(checkDataTypes(3.14))
# 4.2 Conditionals
def evenOrOdd(num):
    if int(num) % 2 == 0:
        return "'Even'"
    else:
        return "'Odd'"
print(evenOrOdd(10))
# 5 Loops
numbers = [1, 2, 3, 4, 5]
def sumWithLoop(numbers):
    sum = 0
    for num in numbers:
        sum += int(num)
    return sum
print(sumWithLoop(numbers))
# 6.1 Lists
letters = ["a", "b", "c"]
def duplicateList(letters):
    newlist = letters[:]
    count = 1
    for item in letters:
        newlist.insert((letters.index(item, 0, len(newlist))+count), item)
        count += 1
    return newlist
print(duplicateList(letters))
# 6.2 Debugging
num = 3
# there was no colon
def square(num):
    return num * num
print(square(num))