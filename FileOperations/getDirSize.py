print("{*} Importing modules")
from os import walk
from os.path import join
from os import system
from os.path import getsize
from sys import argv as args
from sys import exit as leave

def sliceAtPoint(number):
    number = str(number)
    holder = "["
    for k in range(len(number)):
        if number[k] == "e" and number[k+1] == "-":
            return0 = True
            break
        else:
            return0 = False
    for k in range(len(number)):
        if number[k] == ".":
            break
        else:
            holder += number[k]
    holder += "]"
    if return0 == True:
        return "[0]"
    elif return0 == False:
        return holder

try:
    dirf = args[1]
except IndexError:
    print("[!] Error.. Format: getDirSize.py dirname")
    leave()

totalsize = 0

print("{/} Scanning directory..")

for root, dirs, files in walk(dirf, topdown=False):
    for filef in files:
        totalsize += getsize(join(root, filef))

B = totalsize
KB = B/1000
MB = KB/1000
GB = MB/1000
KiB = B/1024
MiB = KiB/1024
GiB = MiB/1024

system("cls")

print("Bytes:", B, sliceAtPoint(B))
print("KB:", KB, sliceAtPoint(KB))
print("MB:", MB, sliceAtPoint(MB))
print("GB:", GB, sliceAtPoint(GB))
print("KiB:", KiB, sliceAtPoint(KiB))
print("MiB:", MiB, sliceAtPoint(MiB))
print("GiB", GiB, sliceAtPoint(GiB))