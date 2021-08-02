import os

DOB = input("Date Of Birth? (DD-MM-YYYY) ")
os.system("echo %DATE% > date0293ffseeernv.pizza")
CurrentDate = open('date0293ffseeernv.pizza', 'r').read()
os.remove('date0293ffseeernv.pizza')
CurrentDate = str(CurrentDate).replace('\n ', '')

def getyear(datef):
    global i
    global holder
    holder = []
    i = 0
    while i<10:
        if i < 6:
            i+=1
            continue
        else:
            holder.append(datef[i])
            i+=1
    returnvar = ""
    for f in range(4):
        returnvar += holder[f]
    return int(returnvar)

dayslived = 0

DOBYear = getyear(DOB)
CurrentYear = getyear(CurrentDate)
Yearf = DOBYear

while Yearf <= CurrentYear:
    if Yearf % 4 == 0:
        dayslived += 366
    elif Yearf % 4 != 0:
        dayslived += 365
    Yearf += 1


def getmonth(datef):
    month = datef[3] + datef[4]
    return int(month)

DOBMonth = getmonth(DOB)
l = 1
monthdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daystosubtract = 0

while l != DOBMonth:
    if l != 2:
        daystosubtract += monthdays[l]
    elif l == 2:
        if DOBYear % 4 == 0:
            daystosubtract += 29
        else:
            daystosubtract += 28
    l += 1

def getday(datef):
    day = datef[0] + datef[1]
    return int(day)

DOBDay = getday(DOB)
daystosubtract += (DOBDay - 1)

CurrentDay = getday(CurrentDate)
CurrentMonth = getmonth(CurrentDate)
j = 12
while j > CurrentMonth:
    if j != 2:
        daystosubtract += monthdays[j]
    elif j == 2:
        if CurrentYear % 4 == 0:
            daystosubtract += 29
        else: 
            daystosubtract += 28
    j = j - 1
daystosubtract += (monthdays[CurrentMonth] -  CurrentDay)

dayslived = dayslived - daystosubtract
yearslived = (CurrentYear - DOBYear) - 1
weekslived = dayslived/7
monthslived = (yearslived * 12) - ((12 - CurrentMonth) + 1)

print("You've lived... ")
print(str(dayslived) + " Days")
print(str(weekslived) + " Weeks")
print(str(monthslived) + " Months")
print(str(yearslived) + " Years")

