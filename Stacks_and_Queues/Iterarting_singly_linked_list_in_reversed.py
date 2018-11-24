# Iterarting_singly_linked_list_in_reversed

# we can use the program written in linked_list section - reversing a sublist time = O(n), 
# space = O(1)


# reverse iterator using stack

def print_linked_listed_in_reverse(head):
	nodes = []
	while head:
		nodes.append(head.data) # push
		head = head.next

	while nodes:
		print(nodes.pop())

# time = O(n)
# space = O(n)