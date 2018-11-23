# base_conversion

#similar to string to integer conversion.


def get_decimal_digits(digit):
	digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	for x in range(len(digits)):
		if digit == digits[x]:
			return x

def hex_to_dec(hexNum):
	decNum = 0

	for digit in range(len(hexNum)):
		decNum *= 16
		decNum = decNum + get_decimal_digits(hexNum[digit])

	return decNum


a = hex_to_dec('FF')
print(a)