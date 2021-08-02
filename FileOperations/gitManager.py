import os
os.system("cls")

if os.path.exists("./.git/") == False:
    try:
        print("[!] Initializing a git repo in current directory")
        os.system("git init")
    except KeyboardInterrupt:
        print("[!] Exiting. Removing git repo... ")
        try:
            os.system("rmdir .git /s /q")
        except:
            os.system("rm -rf .git")

print()
holder = []
holderstr = ""

print("[!] Repo Status")
print()
os.system("git status")
print()
filestoadd = input("Enter the files to add in this format - x, y, z ; leave it empty to add everything in the current dir : ")
print()

def doNothing():
    pass

if filestoadd == "":
    print("[!] Adding all files")
    os.system("git add .")
else:
    for i in range(len(filestoadd)):
        if filestoadd[i] != ',' and filestoadd[i] != ' ':
            holderstr += filestoadd[i]
        elif filestoadd[i] == ' ':
            doNothing()
        elif filestoadd[i] == ',':
            holder.append(holderstr)
            holderstr = ""
        if i == len(filestoadd) - 1:
            holder.append(holderstr)
    filestoadd = holder
    for filE in filestoadd:
        addcmd = "git add " + filE
        print("[%] Adding " + filE)
        os.system(addcmd)

commitMessage = input("Commit message? (This is used to remember the state of your files at the time of committing.) : " )
print()
print("[$] Committing files")
commitCmd = "git commit -m " + commitMessage
os.system(commitCmd)

print()

def push():
    pushOption = input("Push updates? (y/n) ")

    if pushOption == "n" or pushOption == "N":
        pass
    elif pushOption == "y" or pushOption == "Y":
        nameOfRemote = input("What's the remote repository called? (URL/localname) [examples: https://github.com/username/reponame, origin] : ")
        print("[$] Starting push")
        pushCmd = "git push " + nameOfRemote
        os.system(pushCmd)
    else:
        print("[X] Invalid option! ")
        push()

push()

print()
print("[!] Done. Exiting!")
print()
os.system("git status")


