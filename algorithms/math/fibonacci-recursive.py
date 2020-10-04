def fibonacciUn(n,Un_2=None,Un_1=None):
    if(n<1):
        return Un_2 or n
    if (n==1):
        return Un_1 or n
    return fibonacciUn(n-1,Un_2,Un_1) + fibonacciUn (n-2,Un_2,Un_1)
# Test 

print("The first item of the sequence is:")
print(fibonacciUn(1,10,15))

print("The tweleth item of the sequence is:")
print(fibonacciUn(12))