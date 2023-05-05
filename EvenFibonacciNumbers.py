def fibonacciSeq(fir,sec):
	yield fir + sec
	yield from fibonacciSeq(sec,fir+sec)

seq = fibonacciSeq(0,1)
evenSum = 0

for n in seq:
	if n > 4000000:
		break
	if n%2==0:
		evenSum += n

print(evenSum)