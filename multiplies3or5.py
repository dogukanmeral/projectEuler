def sumOfMultiples(num,limit):
	seriesLen = limit / num
	average = seriesLen * (seriesLen+1) / 2
	return (num*average)

print(sumOfMultiples(5,1000))
