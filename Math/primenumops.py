import os

print()
start_no = input("Starting number: ")
end_no = input("Ending number: ")

i = int(start_no)
primenumbers = []
listofprimenumbers = ""


def checkifprime(numero):
    isdivisible = False
    zxy = 2
    while zxy < numero:
        if numero % zxy == 0:
            isdivisible = True
        zxy += 1
    if isdivisible == False:
        return True
    else:
        return False


while i <= int(end_no):
    if checkifprime(i) == True:
        primenumbers.append(i)
    i += 1

wozzy = len(primenumbers)

for primenumber in primenumbers:
    if primenumber != 0 and primenumber != 1:
        listofprimenumbers += str(primenumber)
        listofprimenumbers += ", "
    if primenumber == 0 or primenumber == 1:
        wozzy -= 1

fs = len(listofprimenumbers) - 2

print()
print("-------------------------")
print()
print("Number of prime numbers: " + str(wozzy))

listofprimenumbers = listofprimenumbers[:fs]
print("")
if wozzy != 0:
    print("The prime numbers were: " + listofprimenumbers)
elif wozzy == 0:
    print("The prime numbers were: [None] " )
print()
print("-------------------------")
print()

writetofile = input("Would you like to write the numbers to a file? (y/n) ")

if writetofile == "y" or writetofile == "Y":
    filename = input("Name a file to write to. It will be overwritten if it already exists. ")
    open(filename, 'w').write("Number of prime numbers: " + str(wozzy))
    open(filename, 'a').write('\n')
    open(filename, 'a').write("The prime numbers were: " + listofprimenumbers)
    print("Details written to " + filename + "." + " Bye!")
else:
    print("Okay, goodbye!")