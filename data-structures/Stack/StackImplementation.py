
from sys import maxsize 

def createStack(): 
    stack = [] 
    return stack 

def isEmpty(stack): 
    return len(stack) == 0

def push(stack, item): 
    stack.append(item) 
    print(item + " pushed to stack ") 
    
# Function to remove an item from stack. It decreases size by 1 
def pop(stack): 
    if (isEmpty(stack)): 
        return str(-maxsize -1) # return minus infinite 
    
    return stack.pop() 

# Function to return the top from stack without removing it 
def peek(stack): 
    if (isEmpty(stack)): 
        return str(-maxsize -1) # return minus infinite 
    return stack[len(stack) - 1] 

stack = createStack() 
push(stack, str(10)) 
push(stack, str(20)) 
push(stack, str(30)) 
print(pop(stack) + " popped from stack") 
