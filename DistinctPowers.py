def numOfDistinctPowers(start,end):
	combinations = []

	for base in range(start,end+1):
		for power in range(start,end+1):
			combinations.append(base**power)

	distinctNumbers = [num for i,num in enumerate(combinations) if num not in combinations[:i]]

	return len(distinctNumbers)

print(numOfDistinctPowers(2,100))