# Run_length_encoding/decoding

'''
aaaabbbcccc -- encoding --> 4a3b4c -- decoding --> aaaabbbccc
'''

def decoding(s):
	count = 0
	result = []
	for c in s:
		if c.isdigit():
			count = count * 10 + int(c)
		else: # c is a alphabet
			result.append(c * count) # appends count copies of c to result.
			count = 0

	return ''.join(result)


def encoding(s):
	result = []
	count = 1
	for i in range(1,len(s)+1):
		if i == len(s) or s[i] != s[i-1]:
			# found new characters so write the count of previous character.
			result.append(str(count) + s[i-1])
		else: # s[i] == s[i-1]
			count += 1

	return ''.join(result)

# time complexity  = O(n)