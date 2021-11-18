x1 = float(input('x1: '))
y1 = float(input('y1: '))

x2 = float(input('x2: '))
y2 = float(input('y2: '))

from math import sqrt

d = sqrt(

	pow(x2 - x1, 2)
	+ pow(y2-y1, 2)

)

print(d)
