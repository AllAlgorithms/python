"""Factorial of n (recursive implementation).

@author: Pablo Trinidad <github.com/pablotrinidad>
"""


def factorial(n):
    """Algorithm implementation."""
    return 1 if n <= 0 else n * factorial(n - 1)

n = int(input("Enter an integer n to compute its factorial: "))
print(str(n) + "! = " + str(factorial(n)))
