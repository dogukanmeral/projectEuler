def isSumOfNthPowersOfDigits(num,power):
	return num == sum([int(i)**power for i in str(num)]) and num != 1


def sumOfAllNthPowerNumbers(n):
	return sum([i for i in range(1, 9**n * n) if isSumOfNthPowersOfDigits(i,n)])

print(sumOfAllNthPowerNumbers(5))