# dutch_flag_national_problem

''' write a program that takes an array A and an index into A, and rearranges the elements such
 that all elements less than A[i](the pivot) appear first, followed by elements equal to the pivot,
 followed by elements greater than the pivot.
 '''

''' solution 1: O(n) space complexity O(n) time complexity

simply create 3 lists, lessthan, equalto and greaterthan
compare A and populate new lists

'''

''' solution 2: avoiding O(n) space complexity at the cost of increased time complexity O(n^2)

loop1: move all elements that are less than pivot to the start of the array
loop2: move all elements that are greater than pivot to the end of the array.

chu solution I didn't think this and nobody should ever think like this!
'''

def dutch_flag_partition_s2(pivot_index, A):
	pivot = A[pivot_index]
	print(pivot)
	# first pass group all elements smaller than pivot

	for i in range(len(A)):
		# look for smaller element
		for j in range(i+1,len(A)):
			print(i,j)
			print(A)
			if A[j] < pivot:
				A[i], A[j] = A[j], A[i]
				break

	print(A)
	# second pass group all elements larger than pivot

	for i in reversed(range(len(A))):
		# look for larger element. Stop when we reach an element less than pivot
		# since first pass has moved them to the start.
		for j in reversed(range(i)):
			if A[j] > pivot:
				A[i], A[j] = A[j], A[i]
				break

	print(A)



''' solution 3: better than solution 2 
O(1) space complexity, O(n) time complexity

same logic a better approach!

'''

def dutch_flag_partition_s3(pivot_index, A):
	pivot = A[pivot_index]

	# first pass: group elements smaller than pivot
	smaller = 0

	for i in range(len(A)):
		if A[i] < pivot:
			A[i], A[smaller] = A[smaller], A[i]
			smaller += 1
	print(A)

	# second pass: group elements larger than pivot
	larger = len(A) - 1

	for i in range(len(A) - 1, -1,-1):
		if A[i] > pivot:
			A[i], A[larger] = A[larger], A[i]
			larger -= 1

	print(A)



''' solution 4: sorting in single pass

reduces run time.
4 subarrays --> bottom, middle, top and unclassified

'''

def dutch_flag_partition_s4(pivot_index, A):
	pivot = A[pivot_index]

	# keep the following invariants during partitioning:
	# bottom group: A[:smaller]
	# middle group: A[smaller: equal]
	# unclassified group: A[equal:larger]
	# larger group: A[larger:]

	smaller, equal, larger = 0,0, len(A)

	# keep iterating as long as there is an unclassified element
	while equal < larger:
		# A[equal] is the incoming unclassified element.

		if A[equal] < pivot:
			A[smaller], A[equal] = A[equal], A[smaller]
			smaller += 1
			equal += 1

		elif A[equal] == pivot:
			equal += 1

		else: # A[equal] > pivot
			larger -= 1
			A[larger], A[equal] = A[equal], A[larger]

	print(A)

a = [1,0,2,2,1,1,0,0,2]


dutch_flag_partition_s4(3,a)











