print()
# -- Set Raw Values -- #
date = input('Date (YYYY-MM-DD) : ')
year = int(date[0:4])
month = int(date[5:7])
day = int(date[8:10])

# -- Set Formula Values -- #
f = (14 - month) // 12
y = year - f
m = month + (12*f) - 2
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# -- Apply the formula -- #
answer = days[(day + y + ((31*m) // 12) + (y // 4) - (y // 100) + (y // 400)) % 7] # the formula returns an integer between 0 and 6, and the day at that index of days is the answer

# -- Tell the user the answer -- #
print(f"{date} is a {answer}")
print()
input('[Enter to exit] ')
