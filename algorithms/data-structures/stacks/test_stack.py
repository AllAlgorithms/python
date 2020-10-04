import unittest
from stack import Stack, EmptyStackException

class TestStack(unittest.TestCase):

	def setUp(self):
		self.stack = Stack()

	def test_is_empty(self):
		self.assertTrue(self.stack.is_empty())

	def test_str_and_push(self):
		self.stack.push(6)
		self.assertEqual(str(self.stack),"[6]")

	def test_push_three_elements(self):
		self.stack.push(3)
		self.stack.push(2)
		self.stack.push(1)
		self.assertEqual(str(self.stack),"[1, 2, 3]")

	def test_pop_exception(self):
		with self.assertRaises(EmptyStackException):
			self.stack.pop()

	def test_pop_with_one_element(self):
		self.stack.push("Item")
		self.assertEqual(self.stack.pop(),"Item")
		self.assertTrue(self.stack.is_empty())

	def test_pop_with_two_elements(self):
		self.stack.push(2)
		self.stack.push(1)
		self.assertEqual(self.stack.pop(),1)
		self.assertEqual(str(self.stack),'[2]')

	def test_peek_exception(self):
		with self.assertRaises(EmptyStackException):
			self.stack.peek()

	def test_peek(self):
		self.stack.push(1)
		self.assertEqual(self.stack.peek(),1)

	def test_size(self):
		self.assertEqual(self.stack.size(),0)
		self.stack.push(1)
		self.stack.push(2)
		self.stack.push(3)
		self.assertEqual(self.stack.size(),3)

if __name__ == '__main__':
	unittest.main()