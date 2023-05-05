from CoinSums import CoinSums

def possibleSummations(num):
	return CoinSums(num,[n for n in range(1,num)])

print(possibleSummations(100))