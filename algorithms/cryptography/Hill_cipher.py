import numpy as np
s=list(input("Enter a string"))
c=[]
for i in range(len(s)):
    c.append(ord(s[i])-65)
    
arr= np.array(c)

a1=np.transpose(arr)
print(a1)
a1= a1.reshape(3,1)
print(a1.shape)


#key input
print("Enter the key for the encryption")
R = int(input("rows:")) 
C = int(input("columns:")) 
matrix = [] 
print("Enter the key:") 

for i in range(R):
    a =[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
matrix = np.array(matrix)        
print(matrix.shape)
print(matrix[1][1]) 

mul=np.matmul(matrix,a1)
mul = np.array(mul)
print(mul.shape)
print(mul)
for i in range(R):
    mul[i]=mul[i]%26

print(mul)
