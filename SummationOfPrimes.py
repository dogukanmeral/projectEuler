def floorRoot(n):
	return int((n**(1/2))//1)



def isPrime(n):
	for i in range(2,floorRoot(n)+1):
		if n%i == 0 and n!=i:
			return False
	return True



index = 2
totalSum = 0
while index < 2000000:
	if isPrime(index):
		totalSum += index
	index += 1

print(totalSum)