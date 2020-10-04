#time complexity: O(n log(log n))

def Sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    
    #Here, we mark all the numbers that are not prime
    while(p * p <= n):
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    #only the numbers that are unmarked, are prime. Hence, we print them
    for p in range(2, n):
        if prime[p]:
            print(p, end = ' ')

#driver code
n = int(input())
print("All prime numbers till", n, "are: ")
Sieve(n)
