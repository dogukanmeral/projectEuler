def possibleRoutes(gridSize):
	table = [[1 for _ in range(gridSize+1)] for _ in range(gridSize+1)]
	
	for i in range(1,gridSize+1):
		for j in range(1,gridSize+1):
			table[i][j] = table[i-1][j] + table[i][j-1]

	return table[gridSize][gridSize]

print(possibleRoutes(20))