# Enumerate_all_primes_to_n

'''
write a program that takes an integer argument and returns all the primes between 1 and that integer
Hint: exclude multiples of primes.
'''

''' solution 1: brute force

iterate over all i from 2 to n.
for each i, we test if i is prime; if so we add to results.
we can use trial divisionto test if i is prime, i.e. dividing i by each integer from 2 to square 
root of i, and checking if the reminder is 0. 

complexity --> O(n^ 3/2)
'''

'''
brute force tests each number independently and doesn't exploit the fact that we need to compute ALL
primes from 1 to n.

A better approach is to compute the primes ad when a number is identified as prime, to 'seive' it.
i.e. remove all its multiples from future considerations.

we use a boolean array to encode the candidates, i.e. ith entry in the array is true, then i is 
potentially prime. Initially every number greater than or equal to two is a candidate. Whenever we 
determine a number is prime, we will add it to the result, which is an array. 
'''
# beautiful solution
# time complexity = O(n/2 + n/3 + n/5 + n/7 + ...) ~ O(nloglogn)
# space complexity = O(n)
def generate_primes(n):
	primes = []

	# is_prime[p] represents if p is prime or not. 
	# initially set each to true except 0 and 1.
	# then use seiving to elinimate non primes.

	is_prime = [False, False] + [True] * (n -1)

	for p in range(2, n+1):
		if is_prime[p]:
			primes.append(p)

			# seive p's multiples
			for i in range(p, n+1, p):
				is_prime[i] = False

	return primes


''' more optimized solution is given in the book. '''