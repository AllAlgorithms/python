### Here You can Use this Program For Finding Same elements in two Arrays.
def Array_Inter(arr1,n,arr2,m): ## Here I am Function 
    for i in range(n) :
        for j in range(m) :
            if arr1[i] == arr2[j] :
                print(arr1[i], end = " ")
                break
t=int(input("Test cases: "))  ## take test cases to be run
for k in range(t):
    n=int(input("Size of Array One: ")) ## Size of array one by the user 
    arr1=[int(x) for x in input().split()] ## take inputs from user seperated by space 
    m=int(input("Size Of Array Two: "))  
    arr2=[int(y) for y in input().split()]
Array_Inter(arr1,n,arr2,m)
