"""
    for numbers a, b returns x, y such as x * a + y * b = gcd(a,b)
"""

def extendedEuclidean(a,b):
    a_old, b_old = a,b
    a, b = max(a, b), min(a, b)
    x, y, old_x, old_y = 1, 0, 0, 1
    while b != 0:
        quotient = a // b
        residue = a % b
        a, b = b, residue
        old_x, x = x, (old_x - quotient * x)
        old_y, y = y, (old_y - quotient * y)
    if b_old > a_old:
        return old_x, old_y
    return old_y, old_x


 	
