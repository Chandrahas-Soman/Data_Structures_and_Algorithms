# K_longest_string

'''
write a program that takes a sequence of strings presented in streaming fashin: you cn not back up 
to read an earlier value. Your program must compute k longest strings in a sequence. All that is 
required is the k longest strings- it is not required to order these strings.
'''

'''
As we process the input, we want to track the k longest strings seen so far. Out of these k strings,
the sstring to be evicted when a longer string is to be added is the shorter one. A min-heap (not 
a max heap!) is the right data structure for this application, since it supports eddicient find min,
remove min and insert.
'''
import heapq

def top_k(k, stream):
	# entries are compared by their lengths.
	min_heap = [(len(s) , s) for s in itertools.islice(stream, k)]
	heapq.heapify(min_heap)

	for next_string in stream:
		# push next_string and pop the shortest string in the min_heap
		heapq.heappushpop(min_heap, (len(next_string), s))

	return [p[1] for p in heapq.nsmallest(k, min_heap)]

'''
each string processed in O(logk) time, which is the time to add and to remove the minimum element
from the heap. Therefore, if there are n strings in the input, the time complexity to preocess all of
them is O(nlogk)

we could improve the best case time complexity by firdt comparing the new string's length with 
length of the string at the top of the heap (getting this takes O(1) time) and skipping the insert
if the new string is too short to be in the set.
'''
