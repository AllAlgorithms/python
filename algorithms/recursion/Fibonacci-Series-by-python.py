
### Program to calculate fibonacci series

def fibo(n): // function to calculate fibonacci series
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return(fibo(n-1) + fibo(n-2))
num = int(input("Enter a number: ")) // enter number upto which you want to calculate fibonacci series
for n in range(0,(num+1)):
    print(fibo(n),end=" ")
