# BinaryTreeNode

class BinaryTreeNode:
	def __init__(self, data = None, left =None, right=None):
		self.data = data
		self.left = left
		self.right = right

# tree traversal
def tree_traversal(root):
	if root:
		# preorder: processes root before traversals of left and right children.
		print('Preorder: ')
		print(root.data)

		tree_traversal(root.left)
		# inorder: processes root after the traversal of left child and before the traversal of right
		print('Inorder: ')
		print(root.data)

		tree_traversal(root.right)
		# postorder: processes the root after the traversals of left and right children.
		print('Postorder: ')
		print(root.data)
