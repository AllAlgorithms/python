def cocktailSort(array) 
    n = len(array) 
    swap = 1 
    begin = 0 
    end = n-1 
    #Sorting start 
    while (swap == 1): 
        swap = 0 
        
    #sorting from begin 
        for i in range (begin, end): 
            if (a[i] > a[i+1]) : 
                a[i], a[i+1]= a[i+1], a[i] 
                swap=1 
                
        if (swap==0): 
            break swap = 0 
            
        end = end-1 
        #sorting from end 
        for i in range(end-1, begin-1,-1): 
            if (a[i] > a[i+1]): 
                a[i], a[i+1] = a[i+1], a[i] 
                swap = 1 
        
        begin = begin+1