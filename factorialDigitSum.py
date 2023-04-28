def factorialDigitSum(num):
	for i in range(1,num):
		num *= i
	return sum([int(i) for i in str(num)])

print(factorialDigitSum(100))

