# Test_for_overlapping_cyclefree_lists 

'''
given two singly linked listthere may be list nodes that are common to both (this may not be a bug
- it may be desirable from the perspective of reducing memory dfootprint, as in the flyweight pattern
or maintaining a canonical form.)


write a program that takes two cycle free singly linked lists and determines if there exists a node
that is common to both the list.

Hint: solve the simple cases first.
'''
'''
brute force approach is to store one list's nodes in a hash table, and then iterate through the nodes
of other, testing each for presence in the hash table. time = O(n) space = O(n) n = total number of
nodes in two input lists.

we can avoid extra space by using two nested loops, one iterating through the first list, and the other
to search the second for the node being processed in the first list. However, the time complexity
is O(n^2).

The list overlaps iff both have same tail node: once the lists converge at a node, they can't diverge
at a later node. Therfore, checking for overlap amounts to finding the tail nodes for each of the list.

To find the first overlapping node, we first compute the length of each list. the first overlapping 
node is determined by advancing through the longerlist by the difference in lengths, and then
advancing through both lists in tandem, stopping at first common node. 
If we reach the end of a list without finding a common node the lists do not overlap.
'''

def overlapping_no_cycle_lists(l0,l1):
	def length(L):
		length = 0
		while L:
			length += 1
			L = L.next

	l0_len, l1_len = length(l0), length(l1)
	if l0_len > l1_len:
		l0, l1 = l1, l0 # l1 is the longer list

	# advances the longer list to get equal length lists.
	for _ in range(abs(l1_len - l0_len)):
		l1 = l1.next

	while l0 and l1 and l0 is not l1:
		l0, l1 = l0.next, l1.next
	
	return l0 # None implies there is no overlap between l0 and l1.

# time = O(n), space = O(1)
