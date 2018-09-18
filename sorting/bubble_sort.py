# Python implementation of bubble sort
#
# Author: Carlos Abraham Hernandez

def bubbleSort(arr):
	n = len(arr)

	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

def printArray(arr):
	for i in range(len(arr)):
	    print ("%d" %arr[i]),

# Test
arr = [46, 24, 33, 10, 2, 81, 50]
print ("Unsorted Array:")
printArray(arr)
print ('\n')

bubbleSort(arr)

print ("Sorted Array:")
printArray(arr)
