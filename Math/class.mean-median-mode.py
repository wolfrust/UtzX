classes = []
i = 0
while True:
    i += 1
    try:
        classes.append(input("[^C to stop adding classes] Class {0}: ".format(str(i))))
    except KeyboardInterrupt:
        print('\n')
        break

freqs = []
i = 0
while True:
    try:
        freqs.append(float(input("Frequency of class <<{0}>>: ".format(classes[i]))))
    except IndexError:
        break
    i += 1

modclasses = []
modes = []

for i in range(len(freqs)):
    if freqs[i] == max(freqs):
        modclasses.append(classes[i])

for modc in modclasses:
    l = ""
    for i in range(len(modc)):
        if modc[i] != " " and modc[i] != "-":
            l += modc[i]
        elif modc[i] == "-":
            break
    l = float(l)

    for i in range(len(classes)):
        if classes[i] == modc:
            f1 = freqs[i]
    
    for i in range(len(classes)):
        if classes[i] == modc:
            try:
                f0 = freqs[i - 1]
            except IndexError:
                f0 = 0
    
    for i in range(len(classes)):
        if classes[i] == modc:
            try:
                f2 = freqs[i + 1]
            except IndexError:
                f2 = 0

    upplim = ""
    start = False
    for letter in list(modc):
        if letter == "-":
            start = True
        if start == True and letter != " " and letter != "-":
            upplim += letter
    upplim = float(upplim)
    
    h = upplim - l

    Mode = l + ((f1 - f0)/((2*f1) - f0 - f2)) * h
    modes.append(Mode)


cfs = []
last = 0
for i in range(len(freqs)):
    last += freqs[i]
    cfs.append(last)

n = sum(freqs)

for i in range(len(cfs)):
    if cfs[i] >= n/2:
        mc = classes[i]
        cf = cfs[i - 1]
        f = freqs[i]
        break

l = ""
for i in range(len(mc)):
    if mc[i] != " " and mc[i] != "-":
        l += mc[i]
    elif mc[i] == "-":
        break
l = float(l)

upplim = ""
start = False
for letter in list(mc):
    if letter == "-":
        start = True
    if start == True and letter != " " and letter != "-":
        upplim += letter
upplim = float(upplim)

h = upplim - l

Median = l + ((n/2 - cf)/f) * h



cmarks = []
i = 0 
while True:
    try:
        lowlim = ""
        for index in range(len(classes[i])):
            if classes[i][index] == "-":
                hyphindex = index
                break
            elif classes[i][index] == " ":
                pass
            else:
                lowlim += classes[i][index]
        lowlim = float(lowlim)

        upplim = ""
        for index in range(hyphindex + 1, len(classes[i])):
            if classes[i][index] == " ":
                pass
            else:
                upplim += classes[i][index]
        upplim = float(upplim)

        cmarks.append((upplim + lowlim) / 2)
        i += 1
    except IndexError:
        break


def summation(array):
    sumf = 0
    for number in array:
        sumf += float(number)
    return sumf

fixis = []
for i in range(len(cmarks)):
    fixis.append(float(cmarks[i]) * float(freqs[i]))

mean = summation(fixis) / summation(freqs)

from os import system
system("cls")
system("clear")

print("--------------------------------------")
print("Mean:", str(mean))
print("--------------------------------------")
print("Median:", str(Median))
print("--------------------------------------")
print("Modes: ", modes)
print("--------------------------------------")

print()
input("[EXIT] ")