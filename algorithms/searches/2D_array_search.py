
#it's a searching algorithm for sorted 2D matrix and complexity O(n+m) where n is number of rows and m is number of columns
n,m= map(int,input().split()) #taking row and column input
arr = [[int(input()) for x in range (m)] for y in range(n)] #entering elements into the matrix

k = int(input("enter the search element: "))
flag = False

i,j = 0, m-1
#main algorithm
while((i>=0) and (j>=0) and (i<n) and (j<m)):
    if(arr[i][j] == k):
        flag = True
        break
    elif(arr[i][j]> k):
        j-=1
    else:
        i+=1

if(flag):
    print("element found")
else:        
    print("element not found")
