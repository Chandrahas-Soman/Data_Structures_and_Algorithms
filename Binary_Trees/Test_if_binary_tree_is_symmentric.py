# Test_if_binary_tree_is_symmentric

'''
A binary tree is symmentric if you can draw a vertical line through the rootand then left subtree is
the mirror image of the right subtree. 

write a program that checks whether a binary tree is symmetric.
Hint: definition of symmetry is recursive.
'''

'''
we caan test if a tree is symmetric by computing its mirror image and seeing if the mirror image is 
equal to original tree. computing mirror image of tree is as simple as swapping the left and right
subtrees, and recursively continuing. time and spce = O(n), where n = # of nodes.

the better algorihtm is that we don't need to construct the mirrored subtrees. All that is important 
is whether a pair of subtrees are mirror images. As soon as a pair fails the test, we can short 
circuit the check to false.
'''

def is_symmetric(tree):
	def check_symmentric(subtree_0, subtree_1):
		if not subtree_0 and not subtree_1:
			return True
		elif subtree_0 and subtree_1:
			return (subtree_0.data == subtree_1.data
				and check_symmentric(subtree_0.left, subtree_1.right)
				and check_symmentric(subtree_1.left, subtree_0.right)
				)
		# one subtree is empty
		return False

	return not tree or check_symmentric(tree.left,tree.right)

# time complexity = O(n), space complexity = O(h)