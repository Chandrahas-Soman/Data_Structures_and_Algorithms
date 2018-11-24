# Implementing_stack_with_max_API

'''
Design a stack that includes a max operation, in addition to push and pop. The max operation should
return the maximum element stored in stack.
Hint: use additional storage to track the maximum value.
'''

'''
easiest way is to consider each element in the stack. time complexity = O(n) and space = O(1)

time complexity can be reduced to O(logn) using auxillary datastructure, specifically heap or BST
and a hash table. The space complexity increases to O(n) and the code is quite complex.

suppose we use a single auxillary variable M, to record element that is maximum in the stack.
updating M on pushes is easy: M = max(M,e), where e is the element being pushed.
However, updating M on pop is very time consuming. If M is the element being popped, we have no way of
knowing what is the max remaining element is and are forced to consider all the remaining elements.

we can dramatically improve on the time complexity of popping by caching, in essence trading time
for space. Specifically, for each entry in the stack, we cache maximum stored at below that entry.
Now, when we pop, we evict the corresponding cached value.
'''

class stack_s1:
	ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

	def __init__(self):
		self.element_with_cached_max = []

	def empty(self):
		return len(self.element_with_cached_max) == 0

	def max(self):
		if self.empty():
			raise IndexError('max(): empty stack')
		return self.element_with_cached_max[-1].max

	def pop(self):
		if self.empty():
			raise IndexError('pop(): empty stack')
		return self.element_with_cached_max.pop().element

	def push(self, x):
		self.element_with_cached_max.append(self.ElementWithCachedMax(x, 
			x if self.empty() else max(x, self.max())))


''' each method has O(1) time complexity, additional space complexity is O(n) regardless of storaged
keys.

we can improve the best case needed by observing that if an element e being pushed is smaller than
the maximum element already in the staack, then e can never be maximum, so do not need to record it.
'''

class Stack_s2:
	class Max_With_Count:
		def __init__(self, max, count):
			self.max, self.count = max, count

	def __init__(self):
		self._element = []
		self._cached_max_with_count = []

	def empty(self):
		return len(self._element) == 0

	def max(self):
		if self.empty():
			raise IndexError('max(): empty stack')
		return self._cached_max_with_count[-1].max

	def pop(self):
		if self.empty():
			raise IndexError('max(): empty stack')
		
		pop_element = self._element.pop()
		current_max = self._cached_max_with_count[-1].max

		if pop_element == current_max:
			self.cached_max_with_count[-1].count -= 1
		
			if self._cached_max_with_count[-1].count == 0:
				self._cached_max_with_count.pop()

		return pop_element

	def push(self, x):
		self._element.append(x)
		if len(self._cached_max_with_count) == 0:
			self._cached_max_with_count.append(self.MaxWithCount(x,1))
		else:
			current_max = self._cached_max_with_count[-1].max

			if x == current_max:
				self._cached_max_with_count[-1].count += 1
			elif x > current_max:
				self._cached_max_with_count.append(self.MaxWithCount(x,1))

'''
the worst case  additional space complexity is O(n), which occurs when each key pushed is greater
than all keys in the primary stack. However, when number of distinct keys are small, or the 
maximum changes infrequently, the additional space complexity is less, O(1) in best case.

The time complexity for each specified method is still O(1).
'''