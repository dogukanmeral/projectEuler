def sumOfDiagonals(startNum,spiralSize):
	circles = spiralSize // 2
	diagonals = [1]
	currentNum = startNum

	for circleIndex in range(1,circles+1):
		for _ in range(4):
			currentNum += circleIndex*2
			diagonals.append(currentNum)

	return sum(diagonals) 

print(sumOfDiagonals(1,1001))