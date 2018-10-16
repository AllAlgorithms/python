def main():
	print("Enter the the number")
	n=int(input())
	for i in range(1,n+1):
		b=checkamstrong(i)
		if b:
			print(str(i)+" is an armstrong number")

def checkarmstrong(n):
	t=n
	sum=0
	while t!=0:
		r=t%10
		sum=sum+(r*r*r)
		t=t//10
	if sum==n:
		return True
	else:
		return False

if __name__ == '__main__':
	main()