#
# Python implementation of counting sort.
#
#
# The All ▲lgorithms Project
#
# https://allalgorithms.com/
# https://github.com/allalgorithms/cpp
#
# Contributed by: Simon Faillace Mullen
# Github: @macmullen
#


def counting_sort(arr):
    # Create the counting sort array with length equal to the maximum number
    # in the list.
    count_array = [0] * (max(arr) + 1)
    # Count the amount of repetitions for each number.
    for number in arr:
        count_array[number] += 1
    # Append the amount of repetitions in order.
    position = 0
    for index, number in enumerate(count_array):
        for amount in range(count_array[index]):
            arr[position] = index
            position += 1


arr = [8, 5, 8, 4, 3, 3, 2, 1, 5, 5, 5, 9, 7, 7, 8, 1, 9, 3, 2]
print("Unsorted array:")
print(arr)
counting_sort(arr)
print("Sorted array:")
print(arr)
