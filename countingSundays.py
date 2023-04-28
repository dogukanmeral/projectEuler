firstSundays = 0
monthDays = [31,None,31,30,31,30,31,31,30,31,30,31]

firstDay, month, year = 0,0,1900

def isLeap(year):
    if year%100==0 and year%400!=0:
        return False
    else:
        return year%4==0 

while month != 11 or year != 2000:
    month = month + 1 if month != 11 else 0
    year = year if month != 0 else year + 1
    days = monthDays[month-1] if month-1 != 1  else 29 if isLeap(year) else 28
    
    firstDay = (firstDay + days%7)%7
    
    if firstDay == 6 and year != 1900:
        firstSundays += 1

print(firstSundays)