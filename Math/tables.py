number = int(input("Enter a number: "))
calculateupto = int(input("Calculate up to: "))

for i in range(calculateupto):
    print(number, 'x', i, '=', number*i)
