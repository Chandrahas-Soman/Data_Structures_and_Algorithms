# Interconvert_strings_and_integers

''' implement an integer to string conversion function, and string to integer conversion fucntion
. e.g. if the input to the first function is the integer 314, it should return the string "314".

you can not use library functions like int.

Hint: build the result one digit at a time.
'''

'''
key insight is that for any positive integer x, the least signinficant digit in the decimal 
representation of x is x mod 10, and remaining digits are x/10. this approach computes digits
in reverse order.
e.g. if we begin with 423, we get 3 and we are left with 42 to convert. and so on..

natural algorithm would be to prepend digits to partial reslt. however, adding a digit to the
beginning of a string is expensive, since all the remaining digits have to be moved. A more
efficient way would be to add each computed digit to the end,and then reverse the computed sequence.

if x is negative, we record that, negate x and then add a '-' before reversing. If x is 0, our code
breaks out of the iteration without writing any digits, in which case we need to explicitly set a 
zero.
'''

'''
to convert from a string to an integer we recall the basic working of a postional number system.
A base-10 number d2d1d0 encodes the number 10^2*d2 + 10^1*d1 + 10^0*d0. 

brute force algorithm then is to begin with rightmost digit, and iteratively add 10^i*di to a 
cumulative sum.
the efficient way to compute 10^i+1 is to use existing 10^i and multiply that by 10.

a more elegant solution is to begin from leftmost digit and with each succeeding digit, multipply
the partial result by 10 and add the digit.
e.g. "314"   r = 0
1 iteration  r = 3
2 iteration  r = 3*10 + 1 = 31
3 iteration  r = 31*10 + 4 = 314, which is the final result.

negative numbes are handled by recording the sign and negating the result.
'''

def int_to_str(x):
	is_negative = False
	if x < 0:
		x = -x
		is_negative = True

	s =[]
	while True:
		s.append(chr(ord('0') + x % 10))
		print(s)
		x //= 10
		if x == 0:
			break

	#add the negative sign
	return ('-' if is_negative else '') + ''.join(reversed(s))



def string_to_int(s):
	return functools.reduce(
		lambda running_sum, c: running_sum * 10 + string.digits.index(c),
		s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


'''
a = int_to_str(243)

print(a)

print(chr(ord('0')))

s = []

s.append(ord('0') + 44 %10)
print(s)
s.append(chr(ord('0') + 44%10))
print(s)

'''