numbers = [] #array to hold input numbers [see below]
x = 1

while True:
    try:
        numbers.append(int(input(f"[^C to stop] Enter Number [{x}] : ")))
        x += 1
    except KeyboardInterrupt:
        break

def getfac(num):
    factors = []
    for i in range(1, num, 1):
        if num % i == 0: #i.e. It divides completely (which means it's a factor)
            factors.append(i)
    return factors

fac_all = [] #holds factors of all numbers like [[1, 2, 3], [1, 5, 10, 15]]

for number in numbers:
    fac_all.append(getfac(number)) #append factor arrays to the fac_all array

possible = [] #holds common factors, later in the code max(possible) is taken as the HCF

def isset(val, arr): #check if value exists in array (returns boolean value)
    there = False
    for value in arr:
        if value == val:
            there = True
    return there

#the following loop..
for i in range(len(fac_all)): #iterates through fac_all with index i...
    for factor in fac_all[i]: #iterates through every factor in selected factor array
        set = [] #used later in the loop to check if all numbers contain a factor of the selected factor array
        for x in range(i, len(fac_all), 1): #now, we check if the selected factor (check line 34) is also a factor of other numbers
            if isset(factor, fac_all[x]): #if it is a factor of another number, we append the number to se
                set.append(factor)
        if len(set) == len(fac_all): #so, if set has the same number of values as the number of numbers [len(fac_all)], that means that the selected factor is a factor of every number
            possible.append(set[0]) #in that case, we place that factor in the possible array (as it is a common factor)

print("\n\n")
print("----------------------------")
print()
print(f"\tHCF: [{max(possible)}]") #possible holds the common factors. The highest common factor will be the highest value in possible
print()
print("----------------------------")

print("\n")
input("[Exit] ") #if not run from terminal, make sure it doesn't close abruptly
