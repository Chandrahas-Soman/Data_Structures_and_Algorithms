# sample_offline_data

''' motivation: need for company to select a random subset of its customers to roll out a new feature 
to.
e.g. social networking company may want to see the efect of a new UI on page visit duration without 
taking the chance of aleinating all its users if the roll out is unsuccessful.
'''

'''
implement an algorithm that takes an input as array of distinct elements and a size, and returns a 
subset of given size of the array elements. All subsets should be equally likely. return the result in
input array itself.
hint: how would you construct a random subset of size K+1 given a random subset of size k?
'''

'''
simple approach for input array A of length n and specified size k would be to iterate  through the
input array, selecting entries with probability k/n.

anotehr approach would be, to enumerate all subsets of size k and then select one at random from these.
since there are n choose k subsets of size k, the time and space complexity is huge.

The key of efficiently building a random subset of size k is to first build one of size k-1 and then
adding one element , selected randomly from the rest.

for k = 1, we make one call to random number generator, take the returned value mod n (call it r) and
swap A[0] with A[r]. The entry A[r] holds the result.

for K > 1, we begin bychoosing one element at random as above and mow repeat the sameprocess with the
n-1 element subarray. A[1, n-1], eventually, the random subset occupies the slots A[0, k -1] and 
remaining elements are in the last n - k slots.

Intuitively, if all subsets of size k are equally likely, then the construction process ensures that
the subsets of size k+1 are also equally likely. (mathematical induction)
'''

# time = O(k), space = O(1)
def random_sampling(k, A):
	for i in range(k):
		# generate a random index in [i, len(A) - 1]
		r = random.randint(i, len(A) - 1)
		A[i], A[r] = A[r], A[i]


# the algorithm makes k calls torandom number generator. When k is bigger than n/2, we can optimize
# by computing n-k elements to remove from the set.