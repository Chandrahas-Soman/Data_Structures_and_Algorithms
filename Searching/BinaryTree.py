# Here we will focus on static data stored in sorted order in an array.
# data structures appropriate for dynamic updates are subject to heaps, hash tables and binary search
# trees.

# binary search

def bsearch(t, A):
	L, U = 0, len(A) - 1
	while L <= U:
		M = (L + U) // 2
		if A[M] < t:
			L = M + 1
		elif A[M] == t:
			return M
		else:
			U = M - 1
	return -1

A = [0,1,2,3,4,5,6,7,8]
t = 8
b = bsearch(t, A)

print(b)

# time = O(log n) that is far superior than O(n)
