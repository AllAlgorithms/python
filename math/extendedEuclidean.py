"""
    for numbers a, b returns x, y such as x * a + y * b = gcd(a,b)
"""

def extendedEuclidean(a,b):
    a_old, b_old = a,b
    a, b = max(a, b), min(a, b)
    x, y, old_x, old_y = 0, 1, 1, 0
    while b != 0:
        quotient = a // b
        residue = a % b
        a, b = b, residue
        x, old_x = old_x, (old_x - quotient * x)
        y, old_y = old_y, (old_y - quotient * y)
    if a_old > b_old:
        return x, y
    return y, x


 	
