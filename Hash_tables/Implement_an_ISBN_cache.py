# Implement_an_ISBN_cache

'''
International Statndard Book Number (ISBN) is a unique commercial book identifier. It is a string
of length 10. The first 9 characters are digits; the last character is a check character. The check
character is the sum of first 9 digits mod 11, with 10 represented by X. (modern ISBNs use 13 digits,
and check digit is taken mod 10.)

Create a cache for looking up prices of books identified by their ISBN. For the purpose of this 
exercise, treat ISBNs and prices as positive integers. You must implement a look up, insert and 
erase methods. Use the Least Recenly Used (LRU) policy for cache eviction.

Insert: if an ISBN is already persent, insert should not update the price, but should update that
ISBN tobe most recently used entry.

Lookup: given an ISBN , return the corresponding price; if the element is not present, return -1.
If ISBN is present, update that entry to be the most recently used ISBN.

Erase: remove specified ISBN and corresponding value from the case. Return True if the ISBN was
present; otherwise; return False.

Hint: Amortize the cost of deletion. Alternatively, use the auxiliary data structure.
'''

'''
Hash tables are ideally suited for fast lookups. We can use a hash table to quickly lookup price by 
using ISBNs as keys, and a counter, which we use to record when an operation was performed- every time
we do an insert or lookup we inccrement the counter. For each ISBN we store a value, which is the price
and the timestamp,which is the count corresponding to when that ISBN was most recently inserted or 
looked up.

This approach has O(1) lookup and delete times. Inserts are O(1) time,untilthe cache is full. Once, 
the cache fills up, to add a new ISBN we have to find LRU ISBN, which will be evicted to make place
for the new entry. Finding this entry takes O(n) time, where n is the cache size, since we have to
scan all entries to find the one with smallest timestamp. Therefore, time complexity of insert is 
O(n).

The way to improve efficiency is to avoid processing all ISBNs. Conceptually, the ISBNs are ordered
by when they were most recently used, and we only need to be able to find the oldest ISBN efficiently.
This suggests recording the ISBNs in a queue (in addition to hash table.)

Specifically for each ISBN, we store a reference to its location in the queue. Each time we do a 
lookup on an ISBN, we move to the front of the queue.(This requires us to use a linked list 
implementation of the queue, so that items in the middle of the queue can be moved to the head.) We
do the same when we insert an ISBN thats already present. If an insert results in the queue size 
exceeding n, the ISBN at the tail of the queue is deleted from the cache, i.e., from the queue and 
the hash table.
'''

class LruCache:
	def __init__(self, capacity):
		self._isbn_price_table = collections.OrderedDict()
		self._capacity = capacity

	def lookup(self, isbn):
		if isbn not in self._isbn_price_table:
			return -1
		price = self._isbn_price_table.pop(isbn)
		self._isbn_price_table[isbn] = price
		return price

	def insert(self, isbn, price):
		# we add the value for key only if key is not present - we don't update existing values.
		if isbn in self._isbn_price_table:
			price = self._isbn_price_table.pop()
		elif len(self._isbn_price_table) == self._capacity:
			self._isbn_price_table.popitem(last = False)
		self._isbn_price_table[isbn] = price

	def erase(self, isbn):
		return self._isbn_price_table.pop(isbn,None) is not None

'''
The time complexity for each lookup is O(1) for the hash table lookup and O(1) for updating the 
queue i.e. O(1) overall.