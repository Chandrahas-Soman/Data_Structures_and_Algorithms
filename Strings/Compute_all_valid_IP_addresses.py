# Compute_all_valid_IP_addresses

'''
decimal string is a string consisting of digitss between 0 and 9.

write a program that determines where to add periods to a decimal string so that the resulting string
is a valid IP address. There may be more than one valid IP addresses corresponding to a string,
in which case you should print all possibilities.

Hint: use nested loops
'''

'''
there are three periods in a valid IP address, so we can enumerate all possible placements of these
periods, and check whether all four corresponding substrings are between 0 and 255. We can reduce the
number of placements considered by spacing the periods 1 to 3 characters apart. We can also prune by
stoppoing as soon as substring is not valid.
'''

def get_valid_ip_address(s):
	def is_valid_part(s):
		# '00', '000', '01', etc arenot valid but '0' is valid
		return len(s) == 0 or (s[0] != '0' and int(s) <= 255)

	result = []
	parts = [None] * 4
	for i in range(1,min(4,len(s))):
		parts[0] = s[:i]
		if is_valid_part(parts[0]):
			for j in range(1, min(len(s)-i, 4)):
				parts[1] = s[i:i + j]
				if is_valid_part(parts[1]):
					for k in range(1, min(len(s)-i-j, 4)):
						parts[2] = s[i+j:i+j+k]
						parts[3] = s[i+j+k:]
						if is_valid_part(parts[2]) and is_valid_part(parts[3]):
							result.append('.'.join(parts))

	return result

# total number of IP addresses is constant(2^32) therefore, time complexity = O(1)