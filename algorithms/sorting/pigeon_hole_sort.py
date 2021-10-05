# Python program to implement Pigeonhole Sort Algorithm

def pigeonhole_sort(a):

    # size of range of values in the list
    mini = min(a)
    maxi = max(a)
    size = maxi - mini + 1

    # our list of pigeonholes
    holes = [0] * size

    # Populate the pigeonholes.
    for x in a:
        assert type(x) is int, "integers only please"
        holes[x - mini] += 1

    # Put the elements back into the array in order.
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + mini
            i += 1

# creating an empty list a
a = []

# input the number of element
n = int(input("Enter the number of Elements: "))

# iterating to input the elements
for i in range(0, n):
    element = int(input())

    # appending elements into the list
    a.append(element)

pigeonhole_sort(a)

# printing sorted elements
print("Sorted order is : ", end=' ')

# iterating to print all elements
for i in range(0, len(a)):
    print(a[i], end=' ')

