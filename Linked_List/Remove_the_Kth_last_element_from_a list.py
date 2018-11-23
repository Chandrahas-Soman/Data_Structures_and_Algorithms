# Remove_the_Kth_last_element_from_a list

'''
without knowing the length of the list it is not trivial to delete the Kth element in a singly linked
list.

given a SLL and integer k, write a program to remove the kth last element from the list. Your algorithm
should not use more than a few wordsof storage, regardless of the length of the list. You can't assume
that it is posible to record the length of the list.

hint: if you know the length of the list, can you find kth last node using two iterators?
'''

'''
we use two iterators to traverse the list.The first irterator is advanced by k steps, and then the
two iterators advance in tandem. When first iterator reaches tail, the second iterator is at the
(k+1)th last node and we can remove the kth node.
'''

# assumes L has at least K nodes, deltes the kth last node in L.
def remove_kth_last_node(L,k):
	dummy_head = ListNode(0,L)
	first = dummy_head.next
	for _ in range(k):
		first = first.next

	second = dummy_head

	while first:
		first, second = first.next, second.next

	# second points to te (K+1)th last node, delete its successor.
	second.next = second.next.next

	return dummy_head.next

# time = O(n) space = O(1)
