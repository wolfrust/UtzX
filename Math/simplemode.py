from sys import argv
if len(argv) == 1:
    print("[!] Format: simplemode.py [-d] [-f]")
    print("-> -d : List mode")
    print("-> -f: take input from file, mention whether list is in the file in a vertical (one number/line) format or a horizontal format \n Example: simplemode.py -f [vertical/horizontal]")
    from sys import exit as leave
    input("[EXIT] ")
    leave()
if argv[1] == "-d":
    seq = input("List: ") 
    numbs = []
    num = ""
    for index in range(len(seq)):
        if seq[index] == " ":
            pass
        elif seq[index] == ",":
            numbs.append(float(num))
            num = ""
        elif len(seq) - index == 1:
            num += seq[len(seq) - 1]
            numbs.append(float(num))
        else:
            num += seq[index]
elif argv[1] == "-f":
    filef = input("File: ")
    seq = []
    if argv[2] == "vertical":
        content = open(filef, 'r').readlines()
        for c in content:
            try:
                seq.append(float(str(str(str(c).replace('\n', '')).replace(' ', '')).replace(',', '')))
            except ValueError:
                pass
    elif argv[2] == "horizontal":
        content = open(filef, 'r').read()
        fz = ""
        for letter in content:
            if letter != '\n' and letter != ' ' and letter != '.':
                if letter != ",":
                    fz += letter
                elif letter == ",":
                    seq.append(fz)
                    fz = ""
        for i in range(len(seq)):
            try:
                seq[i] = float(seq[i])
            except ValueError:
                seq.pop(i)
    numbs = seq


freqs = [0]
logged = [0]
for i in range(len(numbs)):
    try:
        freqs[i] = 0
    except IndexError:
        freqs.append(0)
    for m in numbs:
        if numbs[i] == m:
            for l in logged:
                if m == l:
                    logf = True
                    freqs[i] = freqs[i] + 1
                    break
                elif m != l:
                    logf = False
            if logf == False:
                freqs[i] = freqs[i] + 1
                logged.append(m)
            

modeoc = max(freqs)
modes = []
popped = [0]
for i in range(len(freqs)):
    if freqs[i] == modeoc:
        modes.append(numbs[i])

for mode in modes:
    for i in range(len(modes)):
        try:
            if mode == modes[i]:
                for popf in popped:
                    if popf == mode:
                        pf = True
                        break
                    else:
                        pf = False
                if pf == False:
                    modes.pop(i)
                    popped.append(mode)
        except IndexError:
            pass


res = [] 
[res.append(x) for x in modes if x not in res] 

print("--------------------------")
print("Modes: ", res)
print("--------------------------")
