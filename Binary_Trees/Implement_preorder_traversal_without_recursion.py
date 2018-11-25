# Implement_preorder_traversal_without_recursion

'''
write a program which takes as input a binary tree and performs a preorder traversal of the tree. Do
not use recursion. Nodes do not contain parent references.
'''

'''
best way to perform preorder traversal without recursion by noting that preorder traversal visit nodes
in last in first out order. we can perform the preorder traversal using stack of tree nodes. The stack
is initialized to contain the root. we visit a node by popping it, adding first its right child and then
its left child to the stack.
'''

def preorder_traversal(tree):
	path, result = [tree], []

	while path:
		curr = path.pop()

		if curr:
			result.append(curr.data)
			path += [curr.right, curr.left]

	return result

'''
since we push and pop each node exactly once, time complexity = O(n)
space = O(h)