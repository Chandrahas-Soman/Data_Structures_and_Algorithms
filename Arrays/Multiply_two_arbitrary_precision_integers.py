# Multiply_two_arbitrary_precision_integers

''' write a program that takes two arrays representing integers , and returns an integer 
representing their product. 
e.g. since 2 * -70 = -140, if inputs are [2] and [-7,0] your fuction should return the following
array [14]
'''

# hint: use arrays to simulate the grade-school multiplication algorithm

# complexity O(nm)

def multiply(num1, num2):
	sign = 1 
	if (num1[0] < 0) ^ (num2[0] < 0):
		sign = -1

	num1[0], num2[0] = abs(num1[0]), abs(num2[0])

	result = [0] * (len(num1) + len(num2)) # [0,0,0,0, ... ,0]

	for i in reversed(range(len(num1))):
		for j in reversed(range(len(num2))):
			result[i+j+1] += num1[i] * num2[j]
			print(result)
			result[i+j] += result[i+j+1]//10
			print(result)
			result[i+j+1] %= 10
			print(result)

	# remove the leading zeros
	result = result[next((i for i , x in enumerate(result) if x != 0), len(result)):] or [0]

	return [sign * result[0]] + result[1:]


a = multiply([-1,2],[3,3])

print(a)