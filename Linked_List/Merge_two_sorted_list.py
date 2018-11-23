# Merge_two_sorted_list

'''
write a program that takes two lists, assumed to be sorted, and returns their merge. The only field
your program  can change ina node is its next field.

Hint: two sorted arrays can be merged using two indices. For list, take care when one iterator reaches
the end.
'''

from linked_list_structure import ListNode

def merge_two_sorted_lists(L1, L2):
	# create a placeholder for the result.
	dummy_head = tail = ListNode()

	while L1 and L2:
		if L1.data < L2.data:
			temp = tail.next
			tail.next = L1
			L1 = temp

		else:
			temp = tail.next
			tail.next = L2
			L2 = temp

	# appends the remaining nodes of L1 and L2
	tail.next = L1 or L2

	return dummy_head.next

# space = O(1) time = O(n+m)