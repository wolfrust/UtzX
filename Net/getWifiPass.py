from sys import argv
from sys import exit as leave

try:
    if argv[1] == "-h" or argv[1] == "--help" or argv[1] == "help":
            print()
            print("No option: Print to screen and wait for keypress before exit")
            print("-w [FILE]: write output to FILE")
            leave()
except IndexError:
    pass

from os import system #4 - 19 27
system("netsh wlan show profiles > 43pop20.435txt")
profiles = open('43pop20.435txt', 'r').readlines()
from os import remove
remove('43pop20.435txt')

holder = []
for line in profiles:
    fxd = ""
    for letter in range(4, 20):
        try:
            fxd += line[letter]
        except IndexError:
            break
    if fxd == "All User Profile":
        SSID = ""
        for letter in range(27, len(line) - 1):
            SSID += line[letter]
        holder.append(SSID)

networks = holder

for network in networks:
    syscmd = 'netsh wlan show profiles name="' + network + '" key=clear >> 43pop20.435txt'
    system(syscmd)

passfile = open('43pop20.435txt' , 'r').readlines()
passwords = []
for possum in passfile:
    header = ""
    for letter in range(4, 15):
        try:
            header += possum[letter]
        except IndexError:
            break
    if header == "Key Content":
        passwd = ""
        for letter in range(15, len(possum) - 1):
            if possum[letter] != ":" and possum[letter] != " ":
                passwd += possum[letter]
        passwords.append(passwd)

remove('43pop20.435txt')
print()

for netindex in range(len(networks)):
    print("{" + networks[netindex] + "}" + " " + "{" + passwords[netindex] + "}")

print()

try:

    if argv[1] == "-w":
        with open(argv[2], 'w') as outfile:
            for netindex in range(len(networks)):
                outfile.write("{" + networks[netindex] + "}" + " " + "{" + passwords[netindex] + "}")
                outfile.write('\n')

except IndexError:

    input("[ENTER] ")
    leave()