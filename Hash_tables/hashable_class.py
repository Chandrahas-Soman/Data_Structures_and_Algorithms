# Designing_hashable_class

class ContactList:
	def __init__(self, names):
		'''
		names is a list of strings
		'''
		self.names = names

	def __hash__(self):
		# Conceptually we want to hash the set of names. Since the set type is mutable, it can't be
		# hashed. Therefore, we use frozenset.
		return hash(frozenset(self.names))

	def __eq__(self, other):
		return set(self.names) == set(other.names)

	def merge_contact_lists(contacts):
		'''
		contacts is list of ContactList.
		'''
		return list(set(contacts))

''' time complexity of computing a hash is O(n), where n is number of strings in the contact list.
The hash codes are often cached for performance,with the caveat that the cache must be ceared if 
object fields that are referenced by hash function are updated.
