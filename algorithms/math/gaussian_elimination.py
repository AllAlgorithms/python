# Gaussian Elimination algorithm
#
# Author: Gabriel de Souza Nunes

'''
    This is a simple and not very performative Gaussian elimination algorithm. 
    The algorithm consists of apply elementary matrix operations, for take 
    a simple echelon matrix form. For that, three conditional tests are performed

    in range of all number of columns but one:

    First:  if pivot element of the current line and the element just below him of the
            next line is equal zero, then neither operation should be made.

    Second: else if pivot element of the current line is equal zero but the element just below
            him not, then a swap between the lines should made.

    Third:  if none of the above, a sum shoud be made in the all lines below the pivot element
            of the current line so that all the elements below the pivot let be zero.

    After that, the echelon matrix is obtained.
'''

from random import randint

# def elementary matrix operations
def swap_line(matrix: list[list], index1: int, index2: list):
    aux: list = matrix[index1]

    matrix[index1] = matrix[index2]
    matrix[index2] = aux

    return matrix

def mul_line(matrix: list[list], index: int, factor: float):
    matrix[index] = [ x * factor for x in matrix[index] ]

    return matrix

def sum_lines(matrix: list[list], index1: int, index2: int, factor: float = 1):
    aux: list = [ x * factor for x in matrix[index2] ]
    matrix[index1] = [ num + aux[i] for i, num in enumerate(matrix[index1]) ]

    return matrix

def gaussian_elimination(matrix: list[list]):

    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(columns - 1):
        pivot: float = matrix[i][i]
        
        if (pivot == 0 and matrix[i + 1][i] == 0):
            pass
        elif (pivot == 0):
            matrix = swap_line(matrix, 0, 1)
        else:
            for line in range(i + 1, rows):
                if (matrix[line] != 0):
                    factor = -(matrix[line][i] / pivot)
                    matrix = sum_lines(matrix, line, i, factor)
        
    return matrix

def print_matrix(matrix: list):
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(columns):
            print(f'{matrix[i][j]:.2f}', end='\t\t')
        print()


# Tests
matrix = [ [randint(1, 50) for _ in range(5)] for _ in range(5) ]

print("Matrix:")
print_matrix(matrix)

matrix = gaussian_elimination(matrix)

print("\nEchelon Matrix:")
print_matrix(matrix)
