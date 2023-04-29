import string
alphabet = list(string.ascii_uppercase)

def strWorth(text):
	return sum([alphabet.index(c) + 1  for c in text])

def nameScore(index,name):
	return (index+1) * strWorth(name)


with open('Names.txt') as names:
	names = names.read().replace('"',"").split(",")
names.sort()

totalOfScores = sum([nameScore(index,name) for index,name in enumerate(names)])

print(totalOfScores)