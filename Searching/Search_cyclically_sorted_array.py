# Search_cyclically_sorted_array

'''
an array is said to be cyclically sorted if it is possible to cyclically shift its entries so that
it becomes sorted. e.g. [6,7,8,9,1,2,3,4,5] if you cyclically left shift for 4 times then it leads
to sorted array. 

Design O(log n) algorithm for finding the position of the smallest element in a cyclically sorted
array. Assume all elements are distinct. e.g. above arraay should return 4.
'''

'''
for any m, if A[m] > A[n-1], then th minimum value must be an index in the range [m+1:n-1]. 
Conversy, if A[m] < A[n-1], then no in index [m+1, n-1] can be the index of the minimum value.
Note that, it is not possible for A[m] = A[n-1], since it is given that all elements are distinct.
These two observations are the basis for a binary search algorithm.
'''

def search_smallest(A):
	left, right = 0, len(A) - 1
	while left < right:
		mid = (left + right) // 2
		if A[mid] > A[right]:
			# min must be in A[mid+1:right+1]
			left = mid + 1
		else: # A[mid] < A[right]
			# min cant be in A[mid +1:right+1] so it must be in A[left: mid +1]
			right = mid
	# loop ends when left == right
	return left

# time = O(log n)
# this problem cant, in general, be solved in less than linear time when elements are repeated.
# e.g. [1,1,1,1,1,0,1] 0 cant be detected without inspecting every element.