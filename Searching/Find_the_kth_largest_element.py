# Find_the_kth_largest_element

'''
many algorithms require as a subroutine the computation of the kth largest element of an array.
The first largest element is simply the largest element. The nth largest element is smallest 
elements where n is the length of the array.
[3,2,1,5,4] A[3] is the largest element, A[2] is the fifth largest element in A.


Design an algorithm for computing the kth largest element in A.
Hint: Use divide and conquer in conjuction with randomization.
'''

'''
brute force: sort array in descending order and return element at k-1 index. time complexity O(nlogn)

sorting is wasteful. we can use k element min heap, which will lead to O(nlogk) time and O(k) space.
(it computes the k largest elements in sorted order, but all thats asked for is the kth largest 
element)

Conceptually, to focus on the kth largest element in place without completely sorting the array we 
can select an element at random (the pivot) and partition the remaining entries into those greater
than the pivot and those less than the pivot. (since the problem states all elements are distinct
, there cant be any other elements equal to the pivot.) If there are exactly k-1 elements greater 
than the pivot, the pivot must be the kth largest element. If there are more than k-1 elements 
greater than pivot, we can discard elements less than or equal to pivot- k largest element must be 
greater than the pivot. If there are less than k-1 elements greater than pivot, we can discard 
elements greater than or equal to the pivot.
'''

# the numbering starts from one
def find_kth_largest(k, A):
	def find_kth(comp):	
		# Partition A[left:right+1] around pivot_idx, returns the new index of the pivot, 
		# new_pivot_idx, after partition. after partitioning, A[left:new_pivot_idx] contains
		# elements that are 'greater than' the pivot, and A[new_pivot_idx +1: right+1] contains
		# elements that are 'less than' the pivot.
		#
		# "greater than" and 'less than' are defined by comp object.
		#
		# Returns the new index of pivot element after partition.
		def partition_around_pivot(left, right, pivot_idx):
			pivot_value = A[pivot_idx]
			new_pivot_idx = left
			A[pivot_idx] , A[right] = A[right], A[pivot_idx]
			for i in range(left,right):
				if comp(A[i], pivot_value):
					A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
					new_pivot_idx += 1
			A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
			return new_pivot_idx

		left, right = 0, len(A) -1
		while left <= right:
			# generates a random integer in [left,right]
			pivot_idx = random.randint(left, right)
			new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
			
			if new_pivot_idx == k-1:
				return A[new_pivot_idx]
			elif new_pivot_idx > k -1:
				right = new_pivot_idx -1
			else:
				left = new_pivot_idx + 1
	return find_kth(operator.gt)