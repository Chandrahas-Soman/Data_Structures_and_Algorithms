# Finding_the_first_occurance_of_a_substring

''' Strings 6.13
A good string search algorithm is fundamental to performance of many applications. Several clever 
algorithms have been proposed fro string search, each with its own trade-offs. As a result, there is
no single perfect  answer. if someone asks you this question in an interview, the best way to approach
this problem would be to work through one good algorithm in detail and discuss at a high level other
algorithms.

Given two strings s (the "search string") and t (the "text"), find the first occurance of s in t.
Hint: Form a signature from a string.
'''

'''
brute force: twonested loops, first iterate through t, the second tests if s ocuurs starting at the 
current index in t. The worst case complexity is high. O(n^2) text = aa..aaa ntimes, search = aa n/2
times followed by b.

There are three linear time string matching algorothms: KMP, Boyer-Moore, and Rabin-Karp. Of these,
Robin-Karp is by far the simplest to understand and implement.

It is similar to brute force algorithm, but it doesn't require the seond loop. Instead it uses the
concept of a "fingerprint". Specifically, let m be the length of s. It computes hash codes of each 
substring whose length is m-these are the fingerprints. The key to efficiency is using an incremental
has function, such as a function with the property that the hash code of a string is an additive
fucntion of each character. (Such hash function is sometimes referred as rolling hash.) For such a
hash function, getting the hash code of a sliding window of characters is very fast for each shift.

For Rabin-Karp algorithm to run in linear time, we need a good hash function, to reduce the 
likelyhood of collisions, which entail potentially time consuming string equality checks.
'''

def rabin-karp(t,s):
	if len(t) < len(s):
		return -1 # s is not a substring of t

	BASE = 26
	# hash codes for the substring of t and s
	t_hash = functools.reduce(lambda h,c: h * BASE + ord(c), t[:len(s)],0)
	s_hash = functools.reduce(lambda h,c: h * BASE + ord(c), s, 0)
	power_s = BASE**max(len(s)-1,0) # BASE^|s-1|

	for i in range(len(s),len(t)):
		# checks the two substrings are actually eaqual or not, to protect against hash collision
		if t_hash == s_hash and t[i- len(s):i] == s:
			return i - len(s) # match found

		# using rolling has to compute the hash code.
		t_hash -= ord(t[i-len(s)]) * power_s
		t_hash = t_hash * BASE + ord(t[i])

	# tries to match s and t[-len(s):]
	if t_hash == s_hash and t[-len(s):] == s:
		return len(t) - len(s)