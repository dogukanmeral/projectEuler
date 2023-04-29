def sumOfDivisors(n):
	return sum([i for i in range(1,n) if n%i==0])

def isAmicable(n):
	return n == sumOfDivisors(sumOfDivisors(n)) if sumOfDivisors(n) != n else False

def amicablesUnder(n):
	return [i for i in range(1,n) if isAmicable(i)]

print(sum(amicablesUnder(10000)))


