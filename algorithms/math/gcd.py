#EUCLIDEAN ALGORITHM FOR GCD CALCULATION
def computeGCD(x,y):
    while(y):
       x,y= y, x % y
    return abs(x)

print(computeGCD(10,20))
