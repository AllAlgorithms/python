import math

def jumoSearch (listA, theGoalValue):
    length = len(listA)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while length > left &&   theGoalValue >= listA[left]:
        right = min(length - 1, left + jump)
        if listA[left] <= theGoalValue and listA[right] >= theGoalValue:
            break
        left += jump;
    if left >= length or listA[left] > theGoalValue:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and listA[i] <= theGoalValue:
        if listA[i] == theGoalValue:
            return i
        i += 1
    return -1
