# Find_the_missing_IP_address

'''
suppose you were given a file containing roughly one billion IP addresses, each of which is a 32bit 
quantity. How would you programmatically find an IP address that is not in the file. Assume that you 
have unlimited drive space but only a few Mb of RAM at your disposal.

Hint: Can you be sure there is an address which is not in the file?
'''

'''
sort input file and iterate through it, searching for gap between values. time = O(nlogn) To keep 
the RAM usage low, the sort will have to use disk as storage, which in practise is very slow.

good heuristic 255.255.255.255 -- highest value addding one to it leads to an overflow.
0.0.0.0 -- lowest value 

we could add all the IP addresses in the file to a hash table, and enumerate IP addresses starting
from 0.0.0.0, until we find one not in the hash table. This requires min 4 GB of RAM tostore the 
data. 

we can reduce the storage requirement by using bit array representation for the set of all IP address
we allocate an array of 2^32 bits. initialize to 0 and write 1 to everyindex that corresponds to an IP
address in the file. there are 2^32 ~ 4 * 10^9 possible IP address, so not all IP appear in the file.
storage is 2^32 / 8 bytes ~ half GB. This is still in well excess of storage limit.

since input is a file we can make multiple passes through it, we can use this to narrow the search
down to subsets of thespace of all IP address as follows. we make a pass through a file to count 
number of IP addresses present whose leading bit is set to 1, and number of IP addresses whose 
leading bit is 0. At least one IP address must exist which is not in the file, so atleast one of
these two counts is below 2^31. e.g. suppose we have determined using counting that there must be
an IP address which begins with 0 and is absent from the file. We can focus our attention on IP
addresses in that file that begin with 0, and continue the preocess of elimination based on the
second bit. This entails 32 passes and uses only two integer-valued count variable as storage.

since we have more storage, we can count on groups of bits. specificaly, we can count the number
of IP addresses in the that begin with 0,1,2, ... , 2^16 -1 using 2^16 integers that can be 
represented with 32 bits.  for every IP address in the file, we take its 16 MSBs to index into 
this array and increment the count of that number. since file contains fewer than 2^32 numbers,
there must be one entry in the array that is less than 2^16. This tells us that there must be
at least one IP address which has those upper bits and is not in the file. In the second pass,
we can focus only on the addresses whose leading bits match the one we have found, and use a bit
array of size 2^16 to identify a missing address. 
'''

def find_missing_element(stream):
	NUM_BUCKET = 1 << 16
	counter = [0] * NUM_BUCKET
	stream ,stream_copy = itertools.tee(stream)
	for x in stream:
		upper_part_x = x >> 16
		counter[upper_part_x] += 1

	# look for an bucket that contains less than (1 << 16) elements.
	BUCKET_CAPACITY = 1 << 16
	candidiate_bucket = next( 
		i for i, c in enumerate(counter) if c < BUCKET_CAPACITY)

	# finds all IP addresses in the stream whose first 16 bits are equal to candidate_bucket
	candidates = [0] * BUCKET_CAPACITY
	stream = stream_copy
	for x in stream_copy:
		upper_part_x = x >> 16
		if candidate_bucket == upper_part_x:
			# record the presence of 16 LSB of x
			lower_part_x = ((1 << 16) - 1) & x
			candidates[lower_part_x] = 1

	# at least one of the LSB combinations is absent
	for i,v in enumerate(candidates):
		if v == 0:
			return (candidate_bucket << 16) | i 

# storage requirement is dominated by count array, i.e. 2^16 integer entries.