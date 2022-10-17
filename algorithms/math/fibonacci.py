'''
In mathematics, the Fibonacci numbers, commonly denoted Fn , form a sequence, the Fibonacci sequence, in which each number is the sum of the two preceding ones. Like for example first two terms of a sequence are 0 and 1. Now its fibonacci sequence will be as follows.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.
'''

def fibonacciUn(Un_2,Un_1,n: int):
    '''
    This function gives two more terms 
    of the fibonacci sequence after 
    given two terms.
    '''
    if(n<1):
        return Un_2
    if (n==1):
        return Un_1
    for i in range(n):
        fib=Un_1+Un_2
        print(fib)
        Un_2=Un_1
        Un_1=fib
    return Un_1

fibonacciUn(10,15,2)