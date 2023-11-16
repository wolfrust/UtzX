from sys import argv # for reading arguments
from sys import exit as die # to exit, especially during dev or in the middle of the script
from os import walk # to crawl a directory tree.. google for more info
from os import rename # to rename files
from os import path # deals with all sorts of path stuff, here we use the join() function


helpArgs = ['--help', '-h', 'help']

if argv[1] in helpArgs:

	helpText = """

	* Utils/toExt by wolfrust*

		
	Format :  toExt.py <<originalExtension>> <<newExtension>> <<folder>>

	The files in <<folder>> with <<originalExtension>> will be renamed so that their extension is now <<newExtension>>

	The operation is recursive

	Example:

		To change the extension of all files in folder 'bop' from '.py' to '.exe',
			Method 1 : toExt.py .py .exe bop 
			Method 2 : toExt.py py exe bop

	"""
	print(helpText)
	die()

origExt = argv[1] # the extension that we want to convert
newExt = argv[2] # the extension we want to convert to
direx = argv[3] # the files in this directory will undergo the conversion process (recursively)

numFilesRenamed = 0 # we display a message at the end, saying X files were renamed
numFails = 0

for root, dirs, files in walk(direx, topdown=True): 
	for filex in files:
		if filex[len(filex) - len(origExt) : len(filex)] == origExt: # if the file ends with the extension we want to convert

			currentName = path.join(root, filex)

			newName = "" 
			newName += filex[0 : len(filex) - len(origExt)] # the file name not including the extension
			newName += newExt 
			newName = path.join(root, newName) 

			try:
				rename(currentName, newName)

				print(f"[+] {currentName} -> {newName} ")
				numFilesRenamed += 1
			except Exception as error:
				print(f"[!] Could not rename {currentName} to {newName}")
				print(error)
				numFails += 1



print(f"\n[*] {numFilesRenamed} files renamed.")

if numFails != 0:
	print(f"[*] Could not rename {numFails} files.")
else:
	print("[*] All files renamed successfully.")

die()


