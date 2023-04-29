def gcd(a,b):
	for i in range(max(a,b),0,-1):
		if a % i == 0 and b % i == 0:
			return i

def lcm(a,b):
	return int((a*b) / gcd(a,b))

prevLcm = 1

'''for i in range(1,20):
	prevLcm = lcm(prevLcm,i)'''


print(lcm(232792560,20))