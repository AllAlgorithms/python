class trienode:
	def __init__(self,character):
		self.character = character
		self.nextnodes = {}
		self.isEnd = False
		self.dataNode = None
	
class trie: # use case: username/password
	def __init__(self):
		self.start = trienode('')
	def insert(self,id,value): # returns true on successful insertion (value == password)
		temp = self.start
		for nextChar in id:
			temp.nextnodes[nextChar] = temp.nextnodes.get(nextChar,trienode(nextChar))
			temp = temp.nextnodes[nextChar]
		if temp.isEnd == True:
			print("ID already Exists!!")
			return False
		temp.isEnd =True
		temp.dataNode = value
		return True
	def findNode(self,id): # returns false if node doesn't exist and true, node if it does
		temp = self.start
		for nextChar in id:
			next = temp.nextnodes.get(nextChar,None)
			if next is None:
				return False,None
			temp = next
		if temp.isEnd == True:
			return True,temp
		else:
			return False,None

if __name__ == '__main__':
	t = trie()
	t.insert('test1',"dummy1")
	t.insert('test2',"dummy2")
	print(t.findNode('test')) # (false,None)
	a,b = t.findNode('test1')
	print(a,b.dataNode) # true,dummy1