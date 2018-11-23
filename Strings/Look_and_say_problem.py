# Look_and_say_problem

'''
the look an say sequence starts with 1. Subsequent numbers are derived by describing the previous
number in terms of consecutive digits. Specifically, to generate an entry of the subsequence from
the previous entry,read off the digits of the previous entry, counting the number of digits in groups
of the same digit.
e.g. 1; one 1
        two 1s
        one 2 and two ones
     1,11,21,1211,111221,312211,13112221,1112213211

write a program that takes as input an integer n and returns nth integer in the look and say
sequence. return the result as a string.

hint: you need to return a string.
'''

def look_and_say(n):
	def next_number(s):
		result = []
		i = 0
		while i < len(s):
			count = 1
			while i + 1 < len(s) and s[i] == s[i+1]:
				i += 1
				count += 1

			result.append(str(count) + str[i])
			i += 1
		return ''.join(result)

	s = '1'
	for _ in range(1,n):
		s = next_number(s)

	return s

# precise complexity is very hard to compute. time = O(n*2^n)