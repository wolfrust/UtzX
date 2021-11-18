# proves that if you take a number n, then 
[ n * (n+1) * (n+2) .... (n*x) ] % (x+1) = 0

def fact(n): # function to find the factorial of 'n'
	f = n
	for i in range(n - 1, 1, -1):
		f *= i
	return f

print("testing factorials from 1-1000..")
for x in range(1, 1000): # tests factorials from 1-10000 -> no anomalies found
	if (fact(x) % x != 0): # meaning upto 10000, fact(x) was always divisible by x
		print(f"anomaly : {x}") # wasn't triggered

# after testing with factorials, I wanted to see if any consecutive numbers showed the same properties
def consec(start, level): # this startes at 'start' (eg. 7) and works down to a level (eg. 4) - with these examples you'd get 7 * 6 * 5 * 4 = 840
	f = start
	for i in range(start - 1, start - level, -1):
		f *= i
	return f

from random import randint 
print("testing consecutive integers for all levels between 1 & 10000..")
for x in range(1, 10000): # testing for all **levels** between 1 & 10000
	y = randint(10, 500) # random integer between 10 and 500.. what the starting number is doesn't matter for this test
	if (consec(y, x) % x != 0):
		print(f"anomaly : x={x} y={y}") # wasn't triggered



