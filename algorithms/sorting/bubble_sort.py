# Python implementation of bubble sort
#
# Author: Carlos Abraham Hernandez
# Current Implementation by: Gabriel de Souza Nunes

def bubbleSort(arr):
	n = len(arr)
	end = n - 1
	change = True
	
	while(change):
		change = False

		for i in range(end):
			if arr[i] > arr[i + 1]:
				aux = arr[i]
				arr[i] = arr[i + 1]
				arr[i + 1] = aux

				change = True
				k = i
	end = k
		

def printArray(arr):
	for num in arr:
	    print (num)

# Test
arr = [46, 24, 33, 10, 2, 81, 50]
print ("Unsorted Array:")
printArray(arr)
print ()

bubbleSort(arr)

print ("Sorted Array:")
printArray(arr)
