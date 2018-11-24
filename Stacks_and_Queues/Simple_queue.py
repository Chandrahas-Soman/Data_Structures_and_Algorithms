# Simple_Queue

class Queue:
	def __init__(self):
		self._data = collections.deque()

	def enqueue(self, x):
		self._data.append(x)

	def dequeue(self):
		return self._data.popleft()

	def max(self):
		return max(self._data)

# time complexity of enqueue, dequeue = O(1)
# time complexity of finding the maximum is O(n), n = # of entries
