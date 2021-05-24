def binary_search(l,x,start,end):
    #base case: 1 element in the list
    if(start==end):
        if(l[start]==x):
            return start
        else:
            return -1
    else:
        #divide the array into halves
        mid=(start+end)//2
        #typecasting is changing data types
        if(l[mid]==x):
            return mid
        elif(l[mid]>x):
            #first half
            return binary_search(l,x,start,mid-1)
        else:
            #right half
            return binary_search(l,x,mid+1,end)

l=[20,45,60,60,90]
x=int(input("What element do you need to find? "))
index=binary_search(l,x,0,len(l)-1)
if(index==-1):
    print("Not found")
else:
    print("Element found at : ",index+1)
