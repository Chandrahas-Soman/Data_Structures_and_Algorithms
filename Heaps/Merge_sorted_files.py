# Merge_sorted_files

'''
write a program that takes as input a set of sorted sequences and computes the union of these 
sequences as a sorted sequence. e.g. if input is [3,5,7], [0,6] and [0,6,28], then the output is 
[0,0,3,5,6,6,7,28]
Hint: which part of each sequence is significant as the algorithm executes?
'''

'''
brute force --> concatenate these sequences into a single array and then sort it. The time complexity
is O(nlogn) assuming that there are n elements in total.

This approach doesn't take into consideration that individual sequences are sorted. We can take 
advantage of this fact by restricting our attention to the first remaining element in each 
sequence.Specifically we repeatedly pick the smallest element amongst the first element of each of 
the remaining part of the sequence.

A min heapis ideal for maintaining a collection of elements when we need to add arbitrary values and
extract the smallest element.
'''

import heapq

def merge_sorted_arrays(sorted_arrays):
	min_heap = []
	# builds a list of iterators for each array in sorted_arrays.
	sorted_arrays_list = [iter(x) for x in sorted_arrays]

	# puts first element from each iterator for each array in sorted_arrays.
	for i, it in enumerate(sorted_arrays_list):
		print(i,it)
		first_element = next(it, None)
		print(first_element)
		if first_element is not None:
			heapq.heappush(min_heap, (first_element, i))

	print(heapq)
	result = []
	while min_heap:
		smallest_entry, smallest_array_i = heapq.heappop(min_heap)
		smallest_array_iter = sorted_array_iters[smallest_array_i]
		result.append(smallest_entry)
		next_element = next (smallest_array_iter, None)
		if next_element is not None:
			heapq.heappush(min_heap, (next_element, smallest_array_i))

	return result

# k = # of input sequence --> at the most k elements in heap -- > extract min and insert O(log k)
# O(nlog k) --> merge
# space = O(k) additional

merge_sorted_arrays([[1,2,3],[1,2,3,4,5,5],[2,2]])