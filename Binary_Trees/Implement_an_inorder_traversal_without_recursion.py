# Implement_an_inorder_traversal_without_recursion

'''
write a programwhich takes input as binary tree and performs an inorder traversal of the tree. Do not
use recursion,. Nodes do not contain parent references.
Hint: simulate a function call stack.
'''

'''
recursive solution is trivial- first traverse the left subtree, then visit the root and finally
traverse the right subtree. this algoithm can be converted into an iterative algorithm by using an 
explicit stack. Several implementations are possible; the one below is noteworthy in that it pushes
the current node, and not the right child. Furthermore, it doesn't use visited field.
'''

def inorder_traversal(tree):
	s ,result = [],[]

	while s or tree:
		if tree:
			s.append(tree)
			# going left
			tree = tree.left
		else:
			# going up
			tree = s.pop()
			result.append(tree.data)
			# going right
			tree = tree.right
	return result

# time = O(n), space = O(h)