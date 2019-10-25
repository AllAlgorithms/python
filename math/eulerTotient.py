from math import sqrt

"""
this function calculate euler totien function
"""
def eulerTotienFunction(n):
	if n == 1:
		return 1
	result = 1
	temp = n
	for i in range(2,int(sqrt(n))+10):
		if (temp % i == 0):
			j = 0
			while(temp % i == 0):
				j += 1
				temp //= i
			result = result * (i**(j-1)) * (i-1)
	if temp == n:
		return n-1
	return result




