def Kadane(array):
	partialSum = bestSum = array[0]
	fromIndex = toIndex = 0

	for i in range(1, len(array)):
		if array[i] > partialSum + array[i]:
			partialSum = array[i]
			fromIndex  = i
		else:
			partialSum += array[i]

		if partialSum >= bestSum:
			bestSum = partialSum
			toIndex = i

	return {
		"fromIndex" 	: fromIndex,
		"toIndex"	: toIndex,
		"bestSum"	: bestSum
	}

n = int(input("Enter the size of the array: "))
print("Input the array")
array = map(int,raw_input().split())

kadane = Kadane(array)
print("Sum: %d  From: %d  To: %d" % (kadane['bestSum'], kadane['fromIndex'], kadane['toIndex']))