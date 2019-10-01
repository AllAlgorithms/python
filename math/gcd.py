def gcd(A, B):
    if B>A:
        A, B = B, A
    while B!=0:
        temp = B
        B = A%B
        A = temp
    return A

print(gcd(10,20))
