
"""
Pascal's triangle is a triangular array of numbers in which those at the ends of the rows are 1 and each of the others is the sum of the nearest two numbers in the row above (the apex, 1, being at the top).
    
"""
print("Welcome to Pascal's traingle:")


n=int(input("Enter number of rows for the pascal's traingle: "))
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
		
		
# printing pascal's triangle
print( " Your Pascal's traiange for the number {}".format(n))
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()
