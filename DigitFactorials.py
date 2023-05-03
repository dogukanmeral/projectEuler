def factorial(number):
	if number != 0:
		for i in range(1,number):
			number*=i
		return number
	return 1

digitFactorials = [factorial(i) for i in range(10)]

def isCuriousNumber(number):
	return sum([digitFactorials[int(i)] for i in str(number)]) == number if number not in [1,2] else False


upperLimit = 0
	
while len(str(upperLimit))*digitFactorials[9] > upperLimit: upperLimit+=1

print(sum([i for i in range(upperLimit) if isCuriousNumber(i)]))