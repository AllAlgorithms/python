def armstrong(number):
	l1=list(number)
	Sum=0
	order=len(l1)
	for i in l1:
		Sum+=(int(i)**order)

	if Sum==int(number):

		print(number,"is an Armstrong number")
	else:

	    print(number,"is not an Armstrong number")



number=input("Enter the number to check for Armstrong : ")
armstrong(number)