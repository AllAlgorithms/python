


"""A magic square is an N×N grid of numbers in which the entries in each row, column and main diagonal sum to the same number (equal to N(N2+1)/2)"""


import numpy as np


print("Hi! Welcome to the magic square algorithm")
print("Please enter the number for which you would want a magic sqaure to be printed. Please enter an odd number")

# The odd number for which the magic square is created is stored in the variable N

N  = int(input())

# create a matrix with values 0 using numpy. The datatype is int for the elements in the matrix
magic_square = np.zeros((N,N), dtype=int)

n = 1
i, j = 0, N//2

# n iterates from 1 to N**2. The loop exits when n is equal to N**2

while n <= N**2:
    # Start in the middle of the first row.
    # (i = 0 and j = N//2 ) and the element at magic_square[i,j] is the middle in the first row.
    # insert n = 1 to begin with at magic_square[i,j]
    magic_square[i, j] = n
    # increment n by 1
    n += 1
    # Move diagonally up and right, wrapping to the first column or last row if the move leads outside the grid

    new_i, new_j = (i-1) % N, (j+1)% N

    # if the cell is already filled with a number, move vertically down one space.
    if magic_square[new_i, new_j]:
        i += 1
    else:
        i, j = new_i, new_j

print(magic_square)
