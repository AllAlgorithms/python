def railencrypt(st,k):
    c = 0
    x = 0
    m =[[0] * (len(st)) for i in range(k)]
    for r in range(len(st)):
        m[c][r] = st[r]
        if x == 0:
            if c == (k-1):
                x = 1
                c -= 1
            else:
                c += 1
        else:
            if c == 0:
                x = 0
                c += 1
            else:    
                c -= 1
           
    result = [] 
    for i in range(k): 
        for j in range(len(st)): 
            if m[i][j] != 0: 
                    result.append(m[i][j]) 
    print("CipherText:","" . join(result))       
 
def raildecrypt(st,k):
    c , x = 0 , 0
    m =[[0] * (len(st)) for i in range(k)]
    for r in range(len(st)):
        m[c][r] = 1
        if x == 0:
            if c == (k-1):
                x = 1
                c -= 1
            else:
                c += 1
        else:
            if c == 0:
                x = 0
                c += 1
            else:    
                c -= 1
    result = []
    c , x = 0 , 0
    for i in range(k): 
        for j in range(len(st)): 
            if m[i][j] == 1:
                m[i][j] = st[x]
                x += 1
    for r in range(len(st)):
        if m[c][r] != 0:
            result.append(m[c][r])
        if x == 0:
            if c == (k-1):
                x = 1
                c -= 1
            else:
                c += 1
        else:
            if c == 0:
                x = 0
                c += 1
            else:    
                c -= 1
    print("PlainText:","" . join(result))

if __name__ == "__main__": 
    string = input("Enter the Message:")
    string = string.upper()
    key = int(input("Enter the Key:"))
    n = int(input("1.Encryption\n2.Decryption\nInput Your choice:"))
    if(n == 1):
        railencrypt(string,key)
    elif(n == 2):
        raildecrypt(string,key)
    else:
        print("Error")
