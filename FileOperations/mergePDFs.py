print("[*] Importing modules")
from os import system, chdir, remove
from time import sleep
from sys import exit as leave
try:
    from PyPDF2 import PdfFileReader, PdfFileWriter
except ModuleNotFoundError:
    system("pip install PyPDF2")
    sleep(10)
    from PyPDF2 import PdfFileReader, PdfFileWriter

def getOS():
    if system("C:") == 0:
        if system("ls") == 0:
            return "cygwin"
        elif system("ls") == 1:
            return "windows"
    elif system("C:") == 1:
        return "linux"
syst = getOS()
def getTree(dirM):
    global syst
    chdir(dirM)
    if syst == "windows":
        system("dir /B > 3490229389.3432909023.420942904")
    elif syst == "linux" or syst == "cygwin":
        system("ls -A > 3490229389.3432909023.420942904")
    dirtree = open('3490229389.3432909023.420942904', 'r').readlines()
    remove('3490229389.3432909023.420942904')
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

directory = input("Directory (non-recursive): ")
outfile = input("Output file: ")
system("cls")
print("[*] Started")
pdfs = []
print("[*] Getting filenames")
for fil in getTree(directory):
    if fil[len(fil) - 3: len(fil)] == "pdf":
        pdfs.append(fil)

pdfw = PdfFileWriter()
for pdf in pdfs:
    pdfr = PdfFileReader(pdf)
    for index in range(pdfr.getNumPages()):
        pdfw.addPage(pdfr.getPage(index))
    print("[*] Added", pdf)

with open(outfile, 'wb') as output:
    print("[*] Writing")
    pdfw.write(output)

print("[*] Done")
input("[Exit] ")
leave()