#FINDING FACTORIAL THROUGH RECURSION
def recursion(n):
    if(n==0):
        return 1
    else:
        return n*recursion(n-1)
a=int(input("Enter The Number You Want The Factorial Of")) #Asking User The Number for the factorial
if(a>=0):            # Checking if the Number is positive or not
    print(recursion())
else:
    print("Enter Valid Positive Number")
