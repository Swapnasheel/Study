
class Node(object):

	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

## A Balanced Tree is considered! O(logN) complexity

class BinarySearchTree(object):

	def __init__(self):
		self.root = None

	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insertNode(data, self.root)

	def insertNode(self, data, rootNode):

		if data < rootNode.data:
			if rootNode.leftChild:
				self.insertNode(data, rootNode.leftChild)
			else:
				rootNode.leftChild = Node(data)
		else:
			if rootNode.rightChild:
				self.insertNode(data, rootNode.rightChild)
			else:
				rootNode.rightChild = Node(data)


	def getMinValue(self):
		if self.root:
			return self.getMin(self.root)

	def getMin(self, rootNode):
		if rootNode.leftChild:
			return self.getMin(rootNode.leftChild)

		return rootNode.data

	def getMaxValue(self):
		if self.root:
			return self.getMax(self.root)

	def getMax(self, rootNode):
		if rootNode.rightChild:
			return self.getMax(rootNode.rightChild)
    
		return rootNode.data

### In-order Traverse

	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root)

	def traverseInOrder(self, rootNode):
		if rootNode.leftChild:
			self.traverseInOrder(rootNode.leftChild)

		print("%s " % rootNode.data)

		if rootNode.rightChild:
			self.traverseInOrder(rootNode.rightChild)


    
## Testing
bst = BinarySearchTree()

bst.insert(10)
bst.insert(15)
bst.insert(5)
bst.insert(6)

print("Minimum value in the tree is", bst.getMinValue())
print("Maximum value in the tree is", bst.getMaxValue())

bst.traverse()







