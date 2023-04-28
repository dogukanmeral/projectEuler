def monthLength(mon, year):
    if mon == 1:
        return 29 if year%400==0 or (year%100==0 ^ year%4==0) else 28
    else:
        return [31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][mon]

def foo(day,mon,year,total):
    if year == 2000 and mon == 11:
        return total

    nextMonthFirstDay = (day + monthLength(mon,year)%7)%7

    foo(nextMonthFirstDay,(mon+1)%12,year if mon!=11 else year+1, total if nextMonthFirstDay!=0 else total+1)


print(foo(0,0,1900,0))


total = 0

while year != 2000 and mon != 11:
    if year != 1900
        