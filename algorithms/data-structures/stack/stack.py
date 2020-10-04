'''
  Created by Luiz Guerra 
  My github github.com/LuizGuerra
'''

class Stack:
  
  def __init__ (.self):
  	head = null
  	count = 0
  
  def append(.self, e):
  	n = Node(e)
  	if count == 0:  		
  		head = n
  		count += 1
  	else:
  		n.next = head.next
  		head = n
  
  def pop(.self):
  	n = head
  	head = head.next
  	return n.element


class Node (e):
  __init__ (.self, e):
    next = null
    element = e
