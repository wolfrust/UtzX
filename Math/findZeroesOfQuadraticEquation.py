def getZeroes(a, b, c):
    from math import sqrt

    try:
        alpha = str((-b + Decimal(str(sqrt(pow(b, 2) - 4*a*c)))) / (2*a))
        beta = str((-b - Decimal(str(sqrt(pow(b, 2) - 4*a*c)))) / (2*a))
    except ValueError:
        alpha = 'i'
        beta = 'i'

    return alpha, beta

from decimal import Decimal
print()
print("Enter the values of a, b and c, \nassuming your equation is of the form ax^2 + bx + c \nwhere the variable is x and a, b and c are constants.\n")

x2coeff = Decimal(input("a : "))
x1coeff = Decimal(input("b : "))
x0coeff = Decimal(input("c : "))

print("\nZeroes :", getZeroes(x2coeff, x1coeff, x0coeff))

input('\n{Hit enter to exit}... ')
