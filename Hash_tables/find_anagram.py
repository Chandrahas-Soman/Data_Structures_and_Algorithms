# find_anagram

'''
write a program that takes as input a set of words and returns groups of anagrams for those words. 
Each group must contain at least two words.
e.g. if input is debitcard, elvis, silent, badcredit, lives, freedom, listen, levis, money theen 
there are three groups of anagrams. 1. debitcard and badcredit. 2. elvis, lives,levis. 3. silent,
listen. (Note that money doesn't appear in any group, since it has no anagrams in the set.)
'''

'''
since anagrams dont depend on ordering of characters in the strings, we can perform the test by 
sorting the character in the string. Two words are anagrams iff they result in equal strings 
after sorting. 

we can form the described grouping of strings by iterating through all strings, and comparing 
each string with all other remaining strings. If two strings are anagrams, we do not consider the
second string again. This leads to an O(n^2mlogm), where n is number of strings and m is the 
maximum string length.

Looking more carefully at the above computation, note that the key idea is to map strings to a
representative. Given any string, its sorted version can be used as a identifier for the anagram
group it belongs to. What we want is a map from a sorted string to the anagrams it corresponds to.
Any time you need to store a set of strings, a hash table is an excellent choice. Our final 
algorithm proceeds by adding sort(s) for each string s in the dictionary to a hash table. The sorted
strings are keys and the values are arrays of the corresonding strings from the original input.
'''

def find_anagrams(dictionary):
	sorted_string_to_anagrams = collections.defaultdict(list)

	for s in dictionary:
		# sorts the string, uses it as a key, and then apppends the original string as another value
		# into hash table.
		sorted_string_to_anagrams[''.join(sorted(s))].append(s)

	return[group for group in sorted_string_to_anagrams.values() if len(group) > 2]

'''
The computation consists of n calls to sort and n insertions into hashtable. Sorting all the keys has
time complexity O(nmlogm). The insertions add a time complexity of O(nm), yeilding O(nmlogm) time
complexity in total.
'''