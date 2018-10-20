from node import Node

class Stack:

	def __init__(self):
		self.head = None

	def __str__(self):
		node = self.head
		list = []
		while node:
			list.append(node.get_item())
			node = node.get_next()
		return str(list)

	def is_empty(self):
		return not self.head

	def push(self, item):
		if not self.head:
			self.head = Node(item)
		else:	
			self.head = Node(item,self.head)

	def pop(self):
		if not self.head:
			raise EmptyStackException('Cannot pop from a empty stack')
		else:
			item = self.head.get_item()

			if self.head.get_next():
				self.head = self.head.get_next()

			else:
				self.head = None

			return item


	def peek(self):
		if not self.head:
			raise EmptyStackException('Cannot peek from an empty stack')
		else:
			return self.head.get_item()

	def size(self):
		count = 0
		node = self.head
		while node:
			count += 1
			node = node.get_next()
		return count

		
class EmptyStackException(Exception):
	pass