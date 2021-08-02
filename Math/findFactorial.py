number = int(input("Number? "))
factorial = 1

while number > 0:
    factorial += factorial * (number - 1)
    number -= 1

print("Factorial: " + str(factorial))