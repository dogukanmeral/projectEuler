def nDigitFibNumber(n):
	previousNum = 0
	currentNum = 1
	currentIndex = 1
	
	while len(str(currentNum)) != n:
		tempNumber = currentNum + previousNum
		previousNum = currentNum
		currentNum = tempNumber
		currentIndex += 1

	return currentIndex

print(nDigitFibNumber(1000))