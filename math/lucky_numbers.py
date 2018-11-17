def generate_lucky_numbers(limit):

    Arr = list(range(-1, limit+3))   #[-1, 0] are two extra elements added to the array.
                                     #It is used to generalize code on line 8 
    
    while len(Arr) > 0:
        
        Arr = [Arr[i] for i in range(2, len(Arr), 2)]     #Drop 1st two elements, from index [2] delete every 2nd number
                                                          # [1st two numbers are Lucky Numbers, so they are dropped]
        Arr = [Arr[i] for i in range(0, len(Arr)) if((i+1)%3 != 0)]     #Delete every 3rd number
        
        if(Arr): print(", ".join(map(str, Arr[:2])), end=", ")     #Print 1st two elements (Lucky Numbers)
        
if __name__ == "__main__":
    generate_lucky_numbers(120)
    print()
