import os
os.system('cls')

sequence = input("Enter the sequence in this format - x, y, z : ")
selection = input("Enter the selection which you want to examine: ")

holder = []
for i in range(len(sequence)):
    if sequence[i] != ',' and sequence[i] != ' ':
        holder.append(sequence[i])
sequence = holder

def findPosInArray(Array, thing):
    poshol = []
    for xlls in range(len(Array)):
        if Array[xlls] == thing:
            poshol.append(xlls + 1)
    return poshol


selectioncount = 0
selectionpositions = findPosInArray(sequence, selection)
for obj in holder:
    if obj == selection:
        selectioncount += 1

print()
print("---")        
print("Sequence: " + str(sequence))
print("Selection: " + str(selection))
print("---")

print()

print("---")
print("The selection appears [" + str(selectioncount) + "] times in the sequence.")
print("The positions the selection is found in the sequence are: " + str(selectionpositions))
print("---")

try:
    input()
except KeyboardInterrupt:
    print()
