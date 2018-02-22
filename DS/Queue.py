# FIFO -- First in first out


class Queue():

	def __init__(self):
		self.queue = []

	def isEmpty(self):
		return self.queue == []

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data

	def sizeOfQueue(self):
		return len(self.queue)

	def peek(self):
		return self.queue[0]

## Testing

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Size of Queue: ", q.sizeOfQueue())

print("Dequeued: ", q.dequeue())
print("Dequeued: ", q.dequeue())

print("Size of Queue: ", q.sizeOfQueue())
print("Peeked: ", q.peek())

print("Is Empty: ", q.isEmpty())



