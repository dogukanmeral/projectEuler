def CoinSums(total, coins):
	table = [[0 for j in range(total+1)] for i in range(len(coins)+1)]

	for row in table:
		row[0] = 1

	for i in range(1,len(coins)+1):
		for j in range(total+1):
			table[i][j] = table[i-1][j] + (table[i][j-coins[i-1]])

	return table[len(coins)][total]

print(CoinSums(200,[1,2,5,10,20,50,100,200]))