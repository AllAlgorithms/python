
# Python Program for iterative binary search.

def itBinarySearch (arr, l, r, x):
    while(r >= l):
        mid = int(l + (r - l)/2)

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        if arr[mid] > x:
            r = mid - 1

        # Else the element can only be present
        # in right subarray
        else:
            l = mid + 1

    return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = itBinarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
