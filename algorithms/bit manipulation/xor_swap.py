from typing import List


def swap(a:int,b:int) -> list :
    a=a^b
    b=b^a
    a=a^b
    return [a,b]

if __name__=="__main__":
    a=int(input("Enter Number 1 : "))
    b = int(input("Enter Number 2 : "))
    AfterSwap= swap(a,b)
    print(f"After Swap : {AfterSwap[0],AfterSwap[1]}")
