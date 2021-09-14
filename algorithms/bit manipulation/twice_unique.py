def twice_unique(arr:list) :
    unique = 0
    for i in arr:
        unique ^= i
    return unique
if __name__=="__main__":
    array = list(map(int,input().split()))
    #sample input 
    # 1 2 2 3 4 4 3
    element = twice_unique(array)
    print(f"Unique element in the array {array} is {element}")
