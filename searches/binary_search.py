def binarySearch(arr, l, r, x): # l is left, r is right, x is search item
    if r >= l:

        mid = l + (r - l)/2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid+1, r, x)

    else:
        # Element is not present in the array
        return -1

# Tests
result = binarySearch([ 2, 3, 4, 10, 40 ], 0, len(arr)-1, 10)
print(result)
