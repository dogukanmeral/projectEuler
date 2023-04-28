def floorRoot(n):
	return int((n**(1/2))//1)



def isPrime(n):
	for i in range(2,floorRoot(n)+1):
		if n%i == 0 and n!=i:
			return False
	return True


def nThPrime(n):
	prime = 0
	curNum = 1
	while prime != n:
		curNum += 1
		if isPrime(curNum):
			prime += 1

	return curNum


print(nThPrime(10001))
