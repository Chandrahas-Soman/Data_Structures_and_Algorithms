# Reverse_a_single_sublist

'''
write a program that takes singly linked list L and two integers s and f as arguments, and reverses 
the order of nodes from the sth node to  fth node, inclusive. The numbering begins at 1. i.e. the head
node is the first node. Do not allocate additional nodes.

Hint: Focus on successor fields which have to be updated.
'''

from linked_list_structure import ListNode


def reverse_sublist(L, start, finish):
	dummy_head = sublist_head = ListNode(0, L)
	for _ in range(1,start):
		sublist_head = sublist_head.next

	# reverses a sublist
	sublist_iter = sublist_head.next
	for _ in range(finish - start):
		temp = sublist_iter.next
		sublist_iter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp

	return dummy_head

# time complexity is dominated by the search for the fth node. O(f)
