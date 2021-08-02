from pyperclip import copy
from sys import argv
from sys import exit as bye


if len(argv) == 1 or argv[1] == '--help' or argv[1] == '-h' or argv[1] == 'help':
    print("""

    copyFileDataToClipboard by Mateo Cruz

    Format: copyFileDataToClipboard.py <<file>>
    Eg: copyFileDataToClipboard.py egg.txt

    -> This should be used from the command line
    -> Provide only one file argument
    -> Only supports non-binary files

    """)
    print()
    input('Enter to exit.. ')
    bye()


try:
    copy(open(argv[1], 'r').read());
except UnicodeDecodeError:
    print("Sorry, can't copy binary files.")
    bye()
