# A Dynamic Programming based solution to compute nCr % p 
  
# Returns nCr % p 
def nCrModp(n, r, p): 
  
    
    C = [0 for i in range(r+1)] 
  
    C[0] = 1 # Top row of Pascal Triangle 
    
    for i in range(1, n+1): 
  
        for j in range(min(i, r), 0, -1): 
  
            # nCj = (n - 1)Cj + (n - 1)C(j - 1) 
            C[j] = (C[j] + C[j-1]) % p 
  
    return C[r] 
  
# Driver Program 
n = 10
r = 2
p = 13
print('Value of nCr % p is', nCrModp(n, r, p))