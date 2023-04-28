def powerDigitSum(num):
	return sum([int(i) for i in list(str(2**num))])

print(powerDigitSum(1000))