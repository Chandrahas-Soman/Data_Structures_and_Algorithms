# Compute_binary_tree_nodes_in_order_of_increasing_depth

'''
depth of a node = distance from root.

given a binary tree, return an array consisting of the keys at the same level.

given a tree               314
                    6              6
              271      561     2        28

it should return [[314],[6,6],[271,561,2,28]]

hint: first think about solving this problem with a pair of queues.
'''

'''
brute force approach might be to write the nodes into an array while simultaneously computing their 
depths. We can use preorder traversal to compute this array- by traversing a node's left child first
we can ensure that nodes at the same depth are sorted from left to right.
Now we can sort this array using a stable sorting algorithm with node depth being the sort key. 

the time complexity is dominated by time taken to sort.  i.e. O(nlogn) and the space complexity O(n)
which is the spacce to store node depths.

Intuitively, since nodes are already presented in a somewhat ordered fashion in the tree, it should
be possible to avoid a full blown sort, there by reducing time complexity. Furthermore, by processing
nodes in order of depth, we do not need to label everynodewith its depth.

In the following, we use a queue of nodes to store nodes at depth i and a queue of nodes at depth i+1.
After all nodes at depth i are processed, we are done with that queue, and can start processing the
queue with nodes at depths i+1, putting the depth i+2 nodes in the new queue.
'''

def binary_tree_depth_order(tree):
	result = []
	if not tree:
		return result

	curr_depth_nodes = [tree]

	while curr_depth_nodes:
		result.append([curr.data for curr in curr_depth_nodes])
		curr_depth_nodes = [child for curr in curr_depth_nodes for child in (curr.left, curr.right)
		if child]

	return result