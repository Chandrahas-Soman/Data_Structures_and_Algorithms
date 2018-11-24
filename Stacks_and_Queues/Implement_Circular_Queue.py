# Implement_Circular_Queue

'''
queue can be implemented using an arrayand two additional dields, beginning and end indices. This 
structure is called circular queue. both enqueue and dequeue have O(1) time complexity.
if array size is fixde, there is a maximum number of entries that can be stored. If the array is 
dynamically resized, the total time for m combined enqueu and dequeue operations is O(m)

impllement a a queue API using an array for storing elements. your API should include a constructor 
function, which takes as argument the initial capacity of queue, enqueue and dequeue functions, and
a function which returns number of elements stored. Implement dyanamic resizing to sopprt storing
arbitrary large number of elements.
Hint: track head and a tail. how can you differentiate a full queue from an empty one?
'''

'''
a brute force approach is to use an array, with the head always at index 0. an additional variable 
tracks the index of the tail  element. Enqueue has O(1) time complexity. However, dequeue has O(n)
since every element has to be left shifted to fill up the space created at index 0.

a better approach is to keep one more variable to keep track the head. This way deque can also be 
performed in O(1). when performing an enqueue on full array, we need to resize the array. we can't
only resize, because this esults in queue elements not appearing contigiously. 
e.g. if array = [a,b,c,d] a = tail, b = head -- resize --> [a,b,c,d,_,_,_,_] if we cant to enqueue
without overwriting or moving elements.
'''

class Queue:
	SCALE_FACTOR = 2

	def __init__(self,capacity):
		self._entries = [None] * capacity
		self._head = self._tail = self._num_queue_elements = 0

	def enqueue(self,x):
		if self._num_queue_elements == len(self._entries): # need to resize
			# make queue elementsappear consecutively.
			self._entries = (self._entries[self._head:] + self._entries[:self._head])
			# reset head and tail.
			self._head  = 0
			self._tail = self._num_queue_elements
			self._entries += [None] * (len(self._entries) * Queue.SCALE_FACTOR - len(self._entries))


		self._entries[self._tail] = x
		self._tail = (self._tail + 1) % len(self._entries)
		self._num_queue_elements += 1

	def dequeue(self):
		if not self._num_queue_elements:
			raise IndxError('empty queue')
		self._num_queue_elements -= 1
		result = self._entries[_head]
		self._head = (self._head + 1) % len(self._entries)
		return result

	def size(self):
		return self._num_queue_elements

# time complexity = O(1) and amortized time complexity of enqueue = O(1)