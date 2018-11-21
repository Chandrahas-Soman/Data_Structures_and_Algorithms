# Permute_the_elements_of_an_array

'''

permutation is a rearrangement of members of sequence into new sequence.
e.g. there are 24 permutations of [a,b,c,d]; some of these are [b,a,c,d], [c,d,a,b] etc.

Given an array A of n elements and a permutaion P, apply P to A.

e.g. permutation [2,0,1,3] applied to A = [a,b,c,d] yeilds array [b,c,a,d]

Hint: Any permutation can be viewed as a set of cyclic permutaions. For an element in a cycle, how 
would you identify if it has been permuted?

'''

'''
solution 1: 
it is simple to apply permutation array to a given array if additional storage is available to write
resulting array.
we allocate a new array B of the same length, set B[P[i]] = A[i] for each i and then copy B to A.
time complexity = O(n)
space complexity = O(n)

but every permutation can be represented by a collection of independent permutations, each of which 
is cyclic, that is, it moves all elements by a fixed offset, wrapping around.  
... space complexity = O(1) however, we array of booleans..

if we don't want to do that, i.e. we want to perform this without explicitly using additional O(n)
storage, we can use the sign bit in the permutation array. Specifically, we subtract n from P[i] 
after applying it. This means that if an entry in P[i] is negative, we have performed the 
corresponding move.
'''

# elegant space = O(1), time = O(n)
def apply_permutation_s1(perm, A):
	for i in range(len(A)):
		# check if the element at index i has not been moved by checking if perm[i] is nonnegative

		next = i
		while perm[next] >= 0:
			A[i], A[perm[next]] = A[perm[next]], A[i]
			temp = perm[next]

			# Subtracts len(perm) from an entry in perm to make it negative,
			# which corresponds that move has been performed.

			perm[next] -= len(perm)
			next = temp

	print(A)
	# restoring perm
	perm[:] = [a + len(perm) for a in perm]



'''
no sign bit, array of booleans
'''

def apply_permutation_s2(perm, A):
	def cyclic_permutation(start, perm, A):
		i, temp = start, A[start]

		while True:
			next_i = perm[i]
			next_temp = A[next_i]
			A[next_i] = temp
			i, temp = next_i, next_temp

			if i == start:
				break

	for i in range(len(A)):
		# traverse the cycle to see if i is the minimum element.
		j = perm[i]
		while j != i:
			if j < i:
				break
			j = perm[j]
		else:
			cyclic_permutation(i, perm ,A)

	print(A)

A = [0,1,2,3]
P = [3,2,1,0]

apply_permutation_s2(P, A)