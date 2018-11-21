# increment an arbitrary-precision integer

'''
write a program which takes an input as array of digits encoding a nonnegative decimal integer D
and updates the array to represent the integer D+1.
e.g. if the input is [1,2,9] then you should update the array to [1,3,0]
'''

'''

brute force --> convert array of digits to actual integer then increament and back to array of digits

limitation -- > if language imposes a limit on the range of values an integer can take, this approach 
will fail on inputs that encode integers outside of that range.
'''
# better solution
def plus_one(A):
	A[-1] += 1

	for i in reversed(range(1,len(A))):
		if A[i] != 10:
			break

		A[i] = 0
		A[i -1] += 1

		if A[0] == 10:
			# there is a carry out, so we need one more digit to store the result.

			A[0] = 1
			A.append(0)
	return A