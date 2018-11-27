# search_sorted_array_for_first_occurance_of_k

'''
binary search commonly asks for the index of any element of a sorted array that is equal to a 
specified element. This problem has a twist in it.

write a method tha takes a sorted array and a key and returns the index of the first occurance of 
that key in the array. Return -1 if the key does not appear in the array.

Hint: what happens when every entry equals k? don't stop when you first see k.
'''

'''
naive approach --> binary search, if k is found traverse backwards from it to find the first 
occurnce. worst case = O(n) when all elements are same.

better approach --> if we see the element at index i equals k, although we don't know whether i is
the first element equal to k, we do know that no subsequent elements can be the first one. 
Therefore, we remove all the elements with index i+1 or more from the candidates.
'''

def search_first_of_k(A, k):
	left, right, result = 0, len(A) - 1, -1

	# A[left:right + 1] is the candidate set
	while left <= right:
		mid = (left + right)//2
		if A[mid] > k:
			right = mid - 1
		elif A[mid] == k:
			result = mid
			right = mid -1 # Nothing to the right of mid can be solution.
		else: # A[mid] < k
			left = mid + 1
	return result

# time complexity = O(n)