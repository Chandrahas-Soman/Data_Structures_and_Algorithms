# Palindrome

# palindrome string is one which reads tthe same when it is reversed.
# space = O(1) time = O(n)
def is_palindromic(s):
	# note that s[~i] = s[-i - 1]
	return all(s[i] == s[~i] for i in range(len(s) // 2))
