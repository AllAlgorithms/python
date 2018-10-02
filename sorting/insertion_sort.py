"""Insertion sort.

@author: Pablo Trinidad <github.com/pablotrinidad>
"""

import random


def insertion_sort(l):
    """Algorithm implementation."""
    for j in range(1, len(l)):
        key = l[j]  # Current value
        i = j - 1  # Left sided neighbor

        # While left-side index is greater than 0 and that the element
        # of the list in that index is greater than the value we are
        # currently comparing, keep switching values.
        while i >= 0 and l[i] > key:
            l[i + 1] = l[i]
            i -= 1

        # Set the last evaluated neighbor index + 1 to the current value
        l[i + 1] = key

    # Return sorted list
    return l


max_value = int(input("Enter the size of the list you want to sort: "))
l = [random.randint(0, max_value + 1) for _ in range(max_value)]

print("Unordered list:\n", l)

sorted_list = insertion_sort(l)
print("\nSorted list:\n", sorted_list)
