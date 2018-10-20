import unittest
from node import Node

class TestNode(unittest.TestCase):

	def setUp(self):
		self.next_node = Node('item 2')
		self.node = Node('item 1',self.next_node)

	def test_str(self):
		self.assertEqual(str(self.node),'[item 1] -> [item 2]')

	def test_get_item(self):
		self.assertEqual(self.node.get_item(),'item 1')

	def test_get_next(self):
		self.assertIs(self.node.get_next(),self.next_node)

	def test_set_item(self):
		self.node.set_item('another item')
		self.assertEqual(self.node.get_item(),'another item')

	def test_set_next(self):
		another_node = Node('another item')
		self.node.set_next(another_node)
		self.assertIs(self.node.get_next(),another_node)

if __name__ == '__main__':
	unittest.main()