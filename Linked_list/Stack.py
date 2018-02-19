# Simple illustration of a Stack - LIFO
# Using Arrays/ Lists

class Stack:

	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		## Here the last item is removed
		## Thus, remove the last item from the list and del its reference

		data = self.stack[-1]
		del self.stack[-1]
		return data

	def peek(self):
		## This method is only used to check what is the lastest item without deleting it

		return self.stack[-1]

	def isEmpty(self):
		return self.stack == []

	def stackSize(self):
		return len(self.stack)

## Testing

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Size of stack is: ", stack.stackSize())

print("Popped: ", stack.pop())
print("Popped: ", stack.pop())

print("Size of stack is: ", stack.stackSize())

print("Peeked: ", stack.peek())




