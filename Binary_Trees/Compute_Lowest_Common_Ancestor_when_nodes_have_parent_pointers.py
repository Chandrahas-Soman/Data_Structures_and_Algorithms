# Compute_Lowest_Common_Ancestor_when_nodes_have_parent_pointers

'''
any two nodes in a binary tree have a common ancestor, namely the root. The lowest common ancestor(LCA)
of any two nodes in a binary tree is the node furthest from the root that is an ancestor of noth nodes.

computing LCA has important applications. e.g. it is essential calculation when rendering webpages,
specifically when computing CSS that is applicable to particular Document Object Model (DOM) element.

Given two nodes in a binary tree, design an algorithm that computes their LCA. Assume that each node
has a parent pointer.
Hint: the problem is easy when both nodes are the same distance from the root.
'''

'''
brute force approach is to store the nodes on the search path from the root to one of the nodes
in a hash table. This is easily done since we can use the parent field. then we go upfrom the 
second node, stopping as soon as we hit a node in the hsah table. The time and space complexity 
are both O(h), where h is the height of the tree.

we know two nodes have a commonancestor, namely root. If nodes are at the same depth, we can move up
the tree in tandem from both nodes, stopping at the first common node, which is LCA. However, if they
are not at the same depth, we need to keep the set of traversed nodes to know when we find the first
common node. we can circumvent having to store these nodes by ascending from deeper node to get the 
same depth as the shallower node, and then performing tandem upward movement.

Computing depth is straightforward since we have the parent field-time complexity is O(h) and the
space complexity is O(1). Once we have depths w can perform the tandem move to get the LCA.

root node has null parent.
'''

def lca(node0, node1):
	def get_depth(node):
		depth = 0
		while node:
			depth += 1
			node = node.parent
		return depth

	depth0, depth1 = map(get_depth, (node0, node1))
	# makes node0 as the deeper node in order to simplify the code.
	if depth0 < depth1:
		node0, node1 = node1, node0

	# ascends from deeper node
	depth_difference = abs(depth0 - depth1)

	while depth_difference:
		node0 = node0.parent
		depth_difference -= 1

	# now ascends both nodes in tandem
	while node0 is not node1:
		node0, node1 = node0.parent, node1.parent
	
	return node0

# time = O(h), space = O(1)