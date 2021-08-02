import os
os.system("cls")

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

def getOS():
    if os.system("C:") == 0:
        if os.system("ls") == 0:
            return "cygwin"
        elif os.system("ls") == 1:
            return "windows"
    elif os.system("C:") == 1:
        return "linux"

def getfilesize(fileM):
    return os.path.getsize(fileM)

def goThruDir(dirM):
    os.chdir(dirM)
    if syst == "windows":
        os.system("dir /B > 3490229389.3432909023.420942904")
    elif syst == "linux" or syst == "cygwin":
        os.system("ls -A > 3490229389.3432909023.420942904")
    dirtree = open('3490229389.3432909023.420942904', 'r').readlines()
    os.remove('3490229389.3432909023.420942904')
    holder = []
    for fi in dirtree:
        if fi != "3490229389.3432909023.420942904\n":
            holder.append(fi)
    dirtree = holder
    holder = []
    for fi in dirtree:
        zem = str(fi).replace("\n", '')
        holder.append(zem)
    dirtree = holder
    return dirtree

def scanDir(directorY):
    os.system("cls")
    dirtree = goThruDir(directorY)
    for fiz in dirtree:
        print("-->", directorY, "<--")
        try:
            os.chdir(fiz)
            isdir = True
            os.chdir("..")
        except:
            isdir = False
        if isdir == False:
            try:
                B = getfilesize(fiz)
                KB = B/1000
                MB = KB/1000
                GB = MB/1000
                KiB = B/1024
                MiB = KiB/1024
                GiB = MiB/1024
                print("File --->", fiz)
                print("Bytes:", B, sliceAtPoint(B))
                print("KB:", KB, sliceAtPoint(KB))
                print("MB:", MB, sliceAtPoint(MB))
                print("GB:", GB, sliceAtPoint(GB))
                print("KiB:", KiB, sliceAtPoint(KiB))
                print("MiB:", MiB, sliceAtPoint(MiB))
                print("GiB", GiB, sliceAtPoint(GiB))
                print()
                input(":[ENTER]")
                os.system("cls")
            except:
                print("[!] Unable to scan " + fiz)
                input(":[ENTER]")
        elif isdir == True:
            print(fiz, ": <DIR>")
            print()
            input(":[ENTER]")
            os.system("cls")

print("[*] Detecting OS")
syst = getOS()
if syst == "windows":
    print("[!] Windows detected - Hidden files will not be scanned")
elif syst == "cygwin":
    print("[!] Cygwin detected.. Hidden files will be be scanned")
elif syst == "linux":
    print("[!] Linux detected.. Hidden files will be scanned")
print()

inputtype = input("Type of input? [single, multi, dir, multidir] [help for help] ")
if inputtype == "help":
    print()
    print("single: single file input")
    print("multi: multiple file input (must be in this format: x,file name with spaces,z)")
    print("directory: a directory (must end with /)")
    print("multidir: multiple directories (must be in this format: x/,y/,z/)")
    print()
    inputtype = input("Type of input? [single, multi, dir, multidir] ")
filE = input("File(s): ")
if inputtype == "single":
    try:
        B = getfilesize(filE)
    except:
        print()
        print("[!] Unable to scan " + filE)
    KB = B/1000
    MB = KB/1000
    GB = MB/1000
    KiB = B/1024
    MiB = KiB/1024
    GiB = MiB/1024
    os.system("cls")
    print("File --->", filE)
    print("Bytes:", B, sliceAtPoint(B))
    print("KB:", KB, sliceAtPoint(KB))
    print("MB:", MB, sliceAtPoint(MB))
    print("GB:", GB, sliceAtPoint(GB))
    print("KiB:", KiB, sliceAtPoint(KiB))
    print("MiB:", MiB, sliceAtPoint(MiB))
    print("GiB", GiB, sliceAtPoint(GiB))
elif inputtype == "multi":
    os.system("cls")
    multiholder = []
    multiholderstr = ""
    for fk in range(len(filE)):
        if filE[fk] != ",":
            multiholderstr += filE[fk]
        else:
            multiholder.append(multiholderstr)
            multiholderstr = ""
    multiholder.append(multiholderstr)
    for fiLe in multiholder:
        try:
            B = getfilesize(fiLe)
            KB = B/1000
            MB = KB/1000
            GB = MB/1000
            KiB = B/1024
            MiB = KiB/1024
            GiB = MiB/1024
            print()
            print("File --->", fiLe)
            print("Bytes:", B, sliceAtPoint(B))
            print("KB:", KB, sliceAtPoint(KB))
            print("MB:", MB, sliceAtPoint(MB))
            print("GB:", GB, sliceAtPoint(GB))
            print("KiB:", KiB, sliceAtPoint(KiB))
            print("MiB:", MiB, sliceAtPoint(MiB))
            print("GiB", GiB, sliceAtPoint(GiB))
            print()
            input(":[ENTER]")
        except:
            print("[!] Unable to scan " + fiLe)
            print()
            input(":[ENTER]")
        os.system("cls")
elif inputtype == "dir":
    scanDir(filE)

elif inputtype == "multidir":
    multiholder = []
    multiholderstr = ""
    for fk in range(len(filE)):
        if filE[fk] != ",":
            multiholderstr += filE[fk]
        else:
            multiholder.append(multiholderstr)
            multiholderstr = ""
    multiholder.append(multiholderstr)
    for directory in multiholder:
        scanDir(directory)
        if directory != "./":
            os.chdir("..")

else:
    print("[!] Invalid input")