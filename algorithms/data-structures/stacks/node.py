class Node:

	def __init__(self,item,next=None):
		self.item = item
		self.next = next

	def __str__(self):
		string = '[' + str(self.item) + ']'
		next = self.next

		while next:
			if next:
				string += ' -> ' + str(next)
				next = next.get_next()

		return string


	def get_item(self):
		return self.item

	def get_next(self):
		return self.next

	def set_item(self,item):
		self.item = item

	def set_next(self,next):
		self.next = next

