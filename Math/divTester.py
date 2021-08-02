import os
os.system("cls")

dividend = int(input("Test divisibility of? "))
divisor = 1 

print()

while divisor <= dividend:
    if dividend % divisor == 0:
        print(dividend, "is divisible by", divisor)
    elif dividend % divisor != 0:
        print(dividend, "is NOT divisible by", divisor)
    divisor += 1

try:
    input()
except KeyboardInterrupt:
    print()
    
    
