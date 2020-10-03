'''
To find factorial of a number
'''
def factorial(num):      #recursive function
	if num==1 or num==0:
		return 1
	else:
		return factorial(num-1)*num    #function calling itself

num=int(input("Enter the number to find factorial:"))
'''
To check whether the number inputted is positive or not
'''
while num<0:
	print("INVALID INPUT !")
	num=int(input("Enter the number to find factorial:"))
'''
function calling
'''	
x=factorial(num)
print("Factorial of ",num," is ",x)