numb = []

while True:
    try:
        numb.append(int(input('Enter an integer (^C to stop): ')))
    except KeyboardInterrupt:
        break
    except ValueError:
        break

print()
print()

divy = []

for x in range(1, min(numb)+1):
    d = True
    if any(num % x != 0 for num in numb):
        d = False
    if d:
        divy.append(x)

print('Common Divisors:', divy)
