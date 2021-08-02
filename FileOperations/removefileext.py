import os

os.system("dir /B > 230492-90mmmmmsswneri.txt")
dirContents = open('230492-90mmmmmsswneri.txt', 'r').readlines()
os.remove('230492-90mmmmmsswneri.txt')

def rmvext(file0):
    dots = []
    f = 0
    filenamewithoutext = ""
    for i in range(len(file0)):
        if file0[i] == ".":
            dots.append(i)
    try:
        lastdot = dots[len(dots) - 1]
        while f < lastdot:
            filenamewithoutext += file0[f]
            f += 1
        file0 = str(file0).replace('\n', '')
        try:
            if file0 != os.path.basename(__file__):
                os.rename(file0, filenamewithoutext)
        except:
            if file0 != "230492-90mmmmmsswneri.txt":
                print("Unable to move " + file0)
    except IndexError:
        pass
for filef in dirContents:
    file1 = str(filef).replace(" \n", '')
    rmvext(file1)
    
