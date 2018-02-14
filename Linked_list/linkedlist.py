# Simple linked-list creation code

class Node(object):

	def __init__(self, data):
		self.data = data
		self.nextNode = None

class LinkedList(object):

	def __init__(self):
		self.head = None
		self.size = 0

	# To check size of the linked list with O(1) complexity

	def insertStart(self, data):
		self.size = self.size + 1
		newNode = Node(data)

		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode

	def size(self):
		return self.size


	# To check size of the linked list with O(n) complexity

	def size2(self):
		actualNode = self.head
		size = 0

		while actualNode is not None:
			size = size + 1
			actualNode = actualNode.nextNode

		return size


	def insertEnd(self, data):

		self.size - self.size + 1
		newNode = Node(data)
		actualNode = self.head

		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode

		actualNode.nextNode = newNode


	def traverselist(self):
		actualNode = self.head

		while actualNode.nextNode is not None:
			print("%d " % actualNode.data)
			actualNode = actualNode.nextNode





			
