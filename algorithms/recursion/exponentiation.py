
def exponentiation(baseNumber, power):
    answer = None
    
    if power == 1:
        answer = baseNumber
    
    elif power == 2:
        answer = baseNumber * baseNumber
    
    else:
        halfAnswer = exponentiation(baseNumber, power//2)
        answer = halfAnswer * halfAnswer
        
        if power%2 == 1:
            answer *= baseNumber
    
    return answer