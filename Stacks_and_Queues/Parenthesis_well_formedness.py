# Parenthesis_well_formedness

'''
write a program that tests if a string made up of characters '(',')','[',']','{' and '}' is well formed

Hint: which left parenthesis does a right parenthesis match with?
'''

'''
if problem was  like this ((()(()))) we could have done the following. starting from the left 
everytime we see a let parenthesis, we store it. Each time we see a right parenthesis, we match it 
with stored left parenthesis. Since there are not brackets or braces, we can simply keep a count of
the number of unmatched left parenthesis.

For general case we do the same, exceppt that we need to explicitly store the unmatched left characters
i.e. left parenthesis, left braces and left brackets. we can't use three counters, because that will
not tell us the lsat unmatched one. A stac  is perfect option for this application.

If we encounter a right character and the stack is empty or the top of the stack is a differnt type
of left character, the right characer is not matched, implying the string is not matched.
'''

def is_well_formed(s):
	left_chars = []
	LOOKUP = {'(':')', '[':']', '{': '}'}

	for c in s:
		if c in LOOKUP:
			left_chars.append(c)
		elif not left_chars or LOOKUP[left_chars.pop()] != c:
			# unmatched right char or mismatched chars
			return False

	return True

# time = O(n)
