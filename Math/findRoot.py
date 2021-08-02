f = int(input("Find root of? "))
x = 0
p = int(input("Root power? "))

while x < f:
    if pow(x, p) == f:
        print("The root is: " + str(x))
        break
    x += 1
