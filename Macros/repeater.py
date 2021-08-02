try:

    from sys import argv
    from os import system 
    from time import sleep 
    from sys import exit as e

    try:
        command = argv[1]
        interval = int(argv[2])
    except IndexError:
        print("[!] Format: repeater.py command interval")
        e()
    except ValueError:
        print("[!] Format: repeater.py command interval")
        e()

    if system('cls') == 0:
        syst = 'win'
    elif system('cls') == 1:
        syst = 'linux'

    while True:
        if syst == 'win':
            system('cls')
        elif syst == 'linux':
            system('clear')
        system(command)
        sleep(interval)

except KeyboardInterrupt:
    print()
    print("[*] Done")