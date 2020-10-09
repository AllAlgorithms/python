
def exponentiation(baseNumber, power):
    answer = None
    
    if power > 1:
        halfAnswer = exponentiation(baseNumber, power//2)
        answer = halfAnswer * halfAnswer
        
        if power%2 == 1:
            answer *= baseNumber
    
    elif power == 1:
        answer = baseNumber
    
    elif power == 0:
        answer = 1
    
    else: # negative power
        answer = 1 / exponentiation(baseNumber, abs(power))
    
    return answer
