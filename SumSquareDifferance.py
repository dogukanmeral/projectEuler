def sumOfNumbers(n):
	return int(n*(n+1)/2)

def squareOfSum(n):
	return int(sumOfNumbers(n)**2)

def sumOfSquares(n):
	return int(n*(n+1)*(2*n+1)/6)

print(squareOfSum(100)-sumOfSquares(100)) 
