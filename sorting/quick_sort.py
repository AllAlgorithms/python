#quick sort implementation in Python by Neville Antony

def partition(arr, down, up): 
    i = ( down - 1 )         
    pivot = arr[up]    
  
    for j in range(down, up): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[up] = arr[up],arr[i+1] 
    return ( i+1 ) 
 
def quickSort(arr, down, up): 
    if down< up: 
        pi = partition(arr, down, up) 
        quickSort(arr, down, pi-1) 
        quickSort(arr, pi+1, up) 
  
arr = [91, 72, 68, 23, 37, 55] 
n = len(arr) 
quickSort(arr,0,n-1) 
print("The sorted array is :") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
