"""
In mathematics, the greatest common divisor (gcd) of two or more integers,
which are not all zero, is the largest positive integer that divides each of the integers. 
For example, the gcd of 8 and 12 is 4.
» https://en.wikipedia.org/wiki/Greatest_common_divisor 

Due to limited recursion depth this algorithm is not suited for calculating the GCD of big integers.
"""

def recGCD(x, y, div = 0):
    # Detemine which integer is greater and set the divisor accordingly
    if div == 0:
        if x > y:
            div = x
        else:
            div = y
    # If both integers can be divided without a remainder the gcd has been found
    if x % div == 0 and y % div == 0:
        return div
    # Decrease divisor by one and try again
    else:
        return recGCD(x, y, div-1)

x = int(input("x = "))
y = int(input("y = "))
print(f"gcd({x}, {y}) = {recGCD(x,y)}")
