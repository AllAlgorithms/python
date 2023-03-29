import math
def encrypt(key, message):
    ciphertext = [] 
    for col in range(key):
        position = col
        while position < len(message):
            ciphertext.append(message[position])
            position += key
    return ''.join(ciphertext)

def decrypt(key, message):
    numOfRows = math.ceil(len(message) / key)
    plaintext = []
    cipher = [*message]
    remainder = len(message)%key
    count=0
    if(remainder != 0):
        for i in range(0,len(message),numOfRows):
            count += 1
            if(count > remainder):
                cipher.insert(i+numOfRows-1,'#')
        cipher.append('#')
        for row in range(numOfRows):
            position = row
            while(position < len(cipher)):
                plaintext.append(cipher[position])
                position += numOfRows
        plaintext = [ele for ele in plaintext if ele != '#']
    else:
        for row in range(numOfRows):
            position = row
            while(position < len(message)):
                plaintext.append(message[position])
                position += numOfRows
    return ''.join(plaintext)
def main():
    while(True):
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        option = int(input("Enter the option: "))
        if(option == 1):
            text = input("Enter the plain text: ")
            k = int(input("Enter the key: "))
            cipher = encrypt(k,text)
            print("Ciphertext: ", cipher)
        if(option == 2):
            text = input("Enter the ciphertext: ")
            k = int(input("Enter the key: "))
            plain = decrypt(k, text)
            print("Plaintext: ", plain)
        if(option == 3):
            break
main()