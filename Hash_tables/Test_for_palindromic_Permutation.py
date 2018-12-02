# Test_for_palindromic_Permutation

'''
Write a program to test whether the letters forming a string can be permuted to forma palindrome.
e.g. 'edited' can be permuted to form 'deified'.

Hint: Find a simple characterization of strings that can be permuted to form a palindrome. 
'''

'''
all characters must occur in pairs for string to be permutable into palindrome, with one exception, 
if the string is of odd length.

'''

def can_form_palindrome(s):
	# a string can be permuted to form a palindrome iff the number of characters whose frequencies
	# is odd is at the most one.
	return sum(v%2 for v in collections.Counter(s).values()) <= 1


'''
time complexity = O(n) where n is length of the string. 
space complexity = O(c) where c is number of distinct characters in the string.