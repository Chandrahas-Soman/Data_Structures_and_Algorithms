# Delete_duplicates_from_sorted_array

''' write a program that takes input as a sorted array and updates it so that all duplicates have
been removed and the remaining elements have been shifted left to fill the emptied indices.
Return the number of valid elements.

O(n) time and O(1) space complexities.
'''

'''
if O(1) space complexity was not concerned then we could have simply solve the problem by iterating
through A recording values that hve not appeared before into a dictionary. (dictionary is used to
determine if a value is new). New values are also written to list.The list is then copied back to A.


Brute force that uses O(1) additional space 
irerate through A testing if A[i] equals A[i+1], and, if so, shift all elements at and after i+2 
to left by one. (only possible because the array is sorted)

If all entries are equal time complexity becomes O(n^2)

'''

def delete_duplicate(A):
	if not A:
		return 0

	write_index = 1

	for i in range(len(A)):
		if A[write_index - 1] != A[i]:
			A[write_index] = A[i]
			write_index += 1

	return write_index 