# Compute_the_next_permutation

'''
There exists exactly n! permutations for n elements. These can be ordered using a dictionarry 
ordering. Define permutation p to appear before permutaion q if in the first place where p q differ
in theiir array representations, starting from index 0, the corresponding entry for p is less than
that of q.
e.g. [2,1,0] > [2,0,1]
'''

'''
write a program that takes as input a permutaion, and returns the next permutaion under dictionary
ordering. If the permutaion is the last permutaion, return aan empty array.
'''

'''
solution:

key insight is thayt we want to increase the permutation by as little as possible.
lets take example of [6,2,1,5,4,3,0]

we start from the right, and look at the longest decreasing suffix, which is [5,4,3,0].
we can no get the next permutaion just by modifying this suffix, since it is already the maximum
it can be.

instead we look at the entry e that appears just before the longest decreasing suffix, which is
1 in our case. (If there is no such element, longest decreasing suffix is the entire permutaion,
the permutation must be [n-1, n-2, ..., 2,1,0], for ehich there is no next permutation.)

observe that e must be less than some entries in the suffix. Intuitively, we should swap e with the
smallest entry in suffix which is larger than e so as to mimize the change to prefix.

so in our case, if we change, e (1) by 3. swappping results in [6,2,3,5,4,1,0]

we are not done yet. the new prefix is the smallest possible for all the permutaions greater than
the initial permutaion, but the new prefix may not be the smallest. (we can get the smallest suffix
by sorting the entries in suffix from smallest to largest)
in our case that yeilds to [0,1,4,5]

for optimization, its not necessary to call a full blown sorting algorithm on suffix. Since the
suffix was intially decreasing, and after replacing s by e it remains decreasing, reversing the 
suffix  has the effect of sorting it from smallest to largest.

Therefore, the general algorithm for computing the next permutaion is:
i) find k such that p[k] < p[k+1] and entries after index k appear in decresing order.
ii) find the smallest p[l] such that p[l] > p[k] (such an l must exist since p[k] < p[k+1])
iii) swap p[l] and p[k] (note that sequence after position k remains in decreasing order)
iv) reverse the sequence after position k.
'''

# space = O(1) time = O(n)
def next_permutaion(perm):
	# find the first entry from right that is smaller than the entry immediately after it.
	inversion_point = len(perm) - 2

	while(inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]):
		inversion_point -= 1

	if inversion_point == -1:
		return []

	# swap the smallest entry after the inversion_point that is greater than perm[inversion_point]
	# since entries in perm are decreasing after inverion point, if we search in reverse order, the 
	# first entry that is greater than perm[inversion_point] is the entry to swap with.

	for i in reversed(range(inversion_point + 1, len(perm))):
		if perm[i] > perm[inversion_point]:
			perm[i], perm[inversion_point] = perm[inversion_point], perm[i]
			break

	# entries in perm must  appear in decreasing order after inversion_point,
	# so we simply reverse these entries to get the smallest dictionary order.
	perm[inversion_point +1 :] = reversed(perm[inversion_point+1:])

	return perm