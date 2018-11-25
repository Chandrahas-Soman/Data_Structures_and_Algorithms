# Test_if_binary_tree_is_height_balanced

'''
a binary tree is said tobe height balanced if for each node in the tree, the difference in the height
of its left and right subtree is at most one. A perfect binary is height-balanced,as is a complete
binary tree. However, a height balanced binary tree does not have to be perfect or complete.

write a program that takes as input the root of a binary tree and checks whether a tree is height
balanced.
Hint: think of a classic binary tree algorithm.
'''

'''
brute force algorithm: compute a height for the tree rooted at each node x recursively. the basic
computation is to compute the height for each node starting from the leaves, and proceeding upwards.
for each node, we check if the difference in heights of left and right children is greater than one.
we can store heights in a hash table, or a new field in the nodes. this entails O(n) sorage and O(n)
time, where n is number of nodes.

we can solve this problem using less storage by observing that we do not need to store the heigts
of all nodes at the same time. Once we are done with a subtree, all we need to know whether it is
height balanced, and if so what its height is. we dont need any information about descendants of the
subtree's root.
'''

def is_balanced_binary_tree(tree):
	BalancedStatusWithHeight = collections.namedtuple(
		'BalancedStatusWithHeight', ('balanced','height'))

	# first value of return value indicates if tree is balanced, and if balanced the second value
	# of the return value is the height of tree.
	def check_balanced(tree):
		if not tree:
			return BalancedStatusWithHeight(True, -1) # base case

		left_result = check_balanced(tree.left)
		if not left_result.balanced:
			# left subtree is not balanced
			return BalancedStatusWithHeight(False, 0)

		right_result = check_balanced(tree.right)
		if not right_result.balanced:
			# right subtree is not balanced
			return BalancedStatusWithHeight(False, 0)

		is_balanced = abs(left_result.height - right_result.height) <= 1

		height = max(left_result.height, right_result.height) + 1
		return BalancedStatusWithHeight(is_balanced, height)

	return check_balanced(tree).balanced


'''
the program implements a postorder traversal with some calls possibly being eliminated because of
early termination. O(h) = space bound, time = O(n)
