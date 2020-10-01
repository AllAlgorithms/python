def fibonacciUn(Un_2,Un_1,n):
    if(n<1):
        return Un_2
    if (n==1):
        return Un_1
    for i in range(n):
        fib=Un_1+Un_2
        Un_2=Un_1
        Un_1=fib
    return Un_1
print(fibonacciUn(10,15,2))