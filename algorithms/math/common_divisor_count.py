


'''

The function takes two integers as input and return the number of common divisors of
that pair



'''
def cd_count(a,b):
	
	if a==0 or b==0:
		return 2      
	a=(-1*a if a<0 else a)
	b=(-1*b if b<0 else b)
	
	result=0
	while a!=0:
		c=a
		a=b%a
		b=c
	
	for i in range(1,int((b**0.5)+1)):
		if b%i==0:
			if b/i==i:
				result=result+1
			else:
				result=result+2
	return result
