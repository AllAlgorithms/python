def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

# Tests

print(search([1,2,3,4,5], 3))
