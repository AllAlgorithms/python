def gcd (small, large) :
    if (small == 0):
        return large 
    else:
        return gcd(large % small, small)


gcdList = [[6, 9], [6, 12], [12, 18], [7, 14], [7, 13]]

for Set in gcdList :
    small = Set[0]
    large = Set[1]
    Gcd=gcd(small, large)
    print(f"GCD for {small} and {large} is {Gcd}")