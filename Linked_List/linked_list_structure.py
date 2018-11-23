class ListNode:
	def __init__(self, data = 0, next=None):
		self.data = data
		self.next = next

def search_list(L, key):
	while L and L.data != key:
		L = L.next
	# if key was not present in the list, L wil have become null.
	return L

# insert a new_node after node.
def insert_after(node, new_node):
	new_node.next = node.next
	node.next = new_node

# delete the node past this one. Assume node is not a tail.
def delete_after(node):
	node.next = node.next.next
