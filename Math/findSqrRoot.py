f = int(input("Find square root of? "))
x = 0

while x < f:
    if x * x == f:
        print("The square root is: " + str(x))
        break
    x += 1
