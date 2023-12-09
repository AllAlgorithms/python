# Python implementation of bubble sort
#
# Author:Abdur rahman

# bubble sort algorithm in easy way 
# bubble sort happens like this, we have to iterate over the array and swap it. 

def bubbleSortAlgo(arr):
    for j in range(len(arr) - 1):
    	for i in range(len(arr) - 1 - j):
         if arr[i] > arr[i + 1]:
            arr[i + 1], arr[i] = arr[i], arr[i +1]
    return arr
        
arr = [23, 21, 1, 2, 4, 529, 100, 8, 3, 5]
print(bubbleSortAlgo(arr))