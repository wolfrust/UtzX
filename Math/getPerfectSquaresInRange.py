init = int(input("Start index: "))
end = int(input("End index: "))

def sr(integer):
    x = -1
    while x < integer:
        s = None
        if x * x == integer:
            s = str(x)
            break
        x += 1
    return s

m = init
ps = []

while m <= end:
    if sr(m) != None:
        ps.append(m)
    m += 1


print()
print("-------------------")
print("Perfect Squares ({0}): {1}".format(len(ps), ps))
print("-------------------")

input()