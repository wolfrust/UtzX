start_no = int(input("Start index: "))
end_no = int(input("End index: "))
testdivby = input("Test divisibility by: ")

f = start_no
numtimesdiv = 0

factors = []

while f <= end_no:
    if f % int(testdivby) == 0:
        factors.append(f)
        numtimesdiv += 1
    f += 1

print()
print(f"Numbers divisible by [{testdivby}] in range [{start_no}-{end_no}]: {factors} ({numtimesdiv})")

print()
input('[EXIT] ')