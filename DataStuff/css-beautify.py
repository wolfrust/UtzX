try:
    from sys import argv 
    from os import remove
    from sys import exit as e

    try:
        if argv[1] == "-h" or argv[1] == "--help" or argv[1] == 'help':
            print("css-beautify.py inputfile outputfile\n")
            print('--help, -h, help: show this help message & exit\n')
            print('inputfile: css code to be beautified')
            print('outputfile: beautified code will be written to this file\n')
            print('Example: css-beautify.py obsf.css lovely.css')
            e()

        text = open(argv[1], 'r').read()
        out = open(argv[2], 'w')
    except IndexError:
        print("Error! Please run `css-beautify.py --help`")
        e()

    nt = '\n\t'

    for letter in range(len(text)):
        if text[letter] != '{' and text[letter] != '}' and text[letter] != ';':
            out.write(text[letter])
        elif text[letter] == '{':
            if text[letter - 1] != ' ':
                out.write(' ')
            out.write(text[letter] + nt)
        elif text[letter] == ';':
            out.write(text[letter] + nt)
        elif text[letter] == '}':
            out.write('\n' + text[letter] + '\n')

    out.close()
    print("[*] Done")
    e()
except KeyboardInterrupt:
    print()
    print("[!] Removing " + argv[2])
    out.close()
    remove(argv[2])
    print("#Bye")
    e()