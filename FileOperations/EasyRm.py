from os import chdir, system, remove, mkdir, rmdir
import os
import sys

directory = input("Directory: ")
chdir(directory)

def gettree(directoryfile):
    contents = open(directoryfile, 'r').readlines()
    holder = []
    for fil in contents:
        if str(fil).replace('\n', '') != "023943022039.3402394023" and str(fil).replace('\n', '') != os.path.basename(__file__):
            holder.append(str(fil).replace('\n', ''))
    return holder

system("dir /B > 023943022039.3402394023")
tree = gettree('023943022039.3402394023')
remove("023943022039.3402394023")

toremove = []

print("Answer with [y]/[n] or [type] to each of these questions")
input("[ENTER]")
system('cls')
for FILE in tree:
    removefile = input("Remove '" + FILE + "' ? ")
    if removefile == "y" or removefile == "Y":
        toremove.append(FILE)
    elif removefile == "type" or removefile == "TYPE":
        print()
        try:
            contents = open(FILE).read()
            print(contents)
        except:
            print("[!] Error: Cannot read file")
        print()
        removefile = input("Remove '" + FILE + "' ? ")
        if removefile == "y" or removefile == "Y":
            toremove.append(FILE)

print("THE FOLLOWING FILES WILL BE DELETED FOREVER: ")
print(toremove)

proceed = input("Proceed? (y/n) ")
if proceed == "y" or "Y":
    for f in toremove:
        try:
            remove(f)
        except:
            rmdir(f)
    print("[*] Files removed successfully")
    input("[EXIT] ")
    sys.exit()
elif proceed == "n" or "N":
    print("[!] Canceling.. No files have been changed")
    input('[EXIT] ')
    sys.exit()


