def binSearch(a, x, low, high):
   #Return True if target is found in indicated portion of a Python list.
   #The search only considers the portion from data[low] to data[high] inclusive.

 if low > high:
     return False # interval is empty; no match
 else:
     mid = (low + high) // 2
     if x == a[mid]: # found a match
        return True
     elif x < a[mid]:
        # recur on the portion left of the middle
        return binSearch(a, x, low, mid - 1)
     else:
        # recur on the portion right of the middle
        return binSearch(a, x, mid + 1, high)
a = [5, 10, 15, 20, 25, 30, 40]
x = 20
low = 0
high = 6
result = binSearch(a, x, low, high)
if result:
    print("The value ", x, " Found")
else:
    print("The value ", x, " Not found")
