# Python3 code to find n-th Fibonacci number 
# Adapted from code by Sharad Bhardwaj
# Approximate value of golden ratio 
PHI = 1.6180339
  
# Fibonacci numbers upto n = 5 
f = [ 0, 1, 1, 2, 3, 5 ] 
  
# Function to find nth 
# Fibonacci number 
def fib ( n ): 
  
    # Fibonacci numbers for n < 6 
    if n < 6: 
        return f[n] 
  
    # Else start counting from 
    # 5th term 
    t = 5
    fn = 5
      
    while t < n: 
        fn = round(fn * PHI) 
        t+=1
      
    return fn 
  
#OUTPUTING 34
print(n, "th Fibonacci Number =", fib(9))
#OUTPUTING 21
print(n, "th Fibonacci Number =", fib(8)) 
#OUTPUTING 13
print(n, "th Fibonacci Number =", fib(7)) 
