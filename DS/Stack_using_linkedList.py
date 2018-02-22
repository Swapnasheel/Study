## Example of Stack using a Linkedlist
##############
#Still working on the POP method!!!!!!
#############

'''
|   |
|   |
|   | <----- Stack
|   |
|___|

'''

class Node(object):

	def __init__(self, data):
		self.data = data
		self.nextNode = None


class Stack():

	def __init__(self):
		self.head = None
		self.size = 0

	def push(self, data):
		self.size = self.size + 1
		newNode = Node(data)

		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			currentNode = newNode
        '''
	def pop(self):
		if self.head is None:
			return

		self.size = self.size - 1

		return currentNode
        '''
	def peek(self):
		return currentNode

	def sizeOfStack(self):
		return self.size


#testing

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Size of stack is : ", stack.sizeOfStack())

print("Popped: ", stack.pop())
print("Popped: ", stack.pop())

print("Size of stack is : ", stack.sizeOfStack())








		 	

