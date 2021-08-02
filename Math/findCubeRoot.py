f = int(input("Find cube root of? "))
x = 0

while x < f:
    if x * x * x == f:
        print("The cube root is: " + str(x))
        break
    x += 1
