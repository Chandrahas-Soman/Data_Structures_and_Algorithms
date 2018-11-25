# Reconstruct_a_binary_tree_from_traversal_data

'''
Many different binary trees yeild the same sequence of keys in an inorder, preorder and post order 
travesral. However, given an inorder traversal and one of any two other traversal orders of binary 
tree, there exists a unique binary tree that yeilds those orders., assuming each node holds distinct
key.

Given an inorder traversal sequence and a preorder traversal sequence of a binary tree write a program
to reconstruct the tree. Assume each node has a unique key.
hint: focus on root
'''

'''
preorder sequence gives us the key of the root node-it is the first node in sequence. The in turn 
allows us to split the inorder sequence into an inorder sequence for the left subtree, followed by
the root,followed by right subtree.
The next insight is that we can use the left subtree inorder sequence to compute the preorder 
sequence for the left subtree from the preorder sequence for the entire tree. A preorder traversal
sequence consists of the root, followed by the preorder traversal sequence of the left subtree 
followed by the preordered traversal of right subtree. We know the number k of nodes in the left
subtree from the location of the root in the inorder traversal sequence. Therefore, subsequence of k 
nodes after the root in the preorder traversal sequence is the preorder traversal sequence for the
left subtree.

e.g. Inorder (l,root,r) = [F,B,A,E,H,C,D,I,G]
Preorder (root, l,r) = [H,B,F,E,A,C,D,G,I]

H is root (from preorder) --> FBAE in left subtree H root and CDIG in right subtree. (from inorder)
tree is                 H
                  FBAE     CDIG

B is the root of H's left subtree (from preorder HB..) Therefore, F is on left of B and AE is on right
(from inorder [F B AE])
tree is                H
                    B     CDIG
                  F   AE

This construction is continued recursively till we get to the leaves. If implemented naively, this 
algorithm has O(n^2) time complexity. Finding root in inorder sequence takes O(n) time. We can 
improve the time complexity by initially build a has table from keys to thier positions in inorder
sequence.
'''

import BinaryTreeNode


def binary_tree_from_preorder_inorder(preorder,inorder):
	node_to_inorder_idx = {data: i for i,data in enumerate(inorder)}

	# build a subtree with preorder[preorder_start: preorder_end] and
	# inorder[inorder_start:inorder_end]
	def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end, inorder_start, inorder_end):

		if preorder_end <= preorder_start or inorder_end <= inorder_start:
			return None

		root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
		left_subtree_size = root_inorder_idx - inorder_start
		return BinaryTreeNode(
			preorder[preorder_start],
			# Recursively builds the left subtree.
			binary_tree_from_preorder_inorder_helper(
				preorder_start + 1, preorder_start + 1 + left_subtree_size,
				inorder_start, root_inorder_idx),
			# Recursively builds the right subtree.
			binary_tree_from_preorder_inorder_helper(
				preorder_start + 1 + left_subtree_size, preorder_end,
				root_inorder_idx + 1, inorder_end)
			)

	return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0 , len(inorder))

# time = O(n) since building hash table = O(n) and recursive reconstruction spends O(1) time per node.
# space = O(n + h)= O(n) -- size of the hash plus maximum depth of the fucntion call stack.