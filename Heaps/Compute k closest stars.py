# Compute k closest stars

'''
consider a coordinate system for milky way in which earth is at (0,0,0). Model stars as points and 
assume distances arein light years. The milky way consists of approax 10^12 stars and their coordinates
are stored in a file.

how would you compute the k stars which are closest to Earth?

Hint: Suppose you know the k closest stars in the first n stars.If (n+1)th star is to be added the
set of k closest stars, which element in that set should be evicted?
'''

'''
max heap is perfect for this application. Conceptually, we start by adding the first k stars to the
max heap. as we process the stars, each time we encounter a new star that is closer to Earth than the
star which is furthest from Earth among the stars in the max_heap, we delete from max heap and add 
new one. Otherwise discard the new star and continue.
'''
import heapq

class Star:
	def __init__(self,x,y,z):
		self.x, self.y, self.z = x, y, z

	@property
	def distance(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def __lt__(self, rhs):
		return self.distance < rhs.distance


def find_closest_k_stars(stars, k):
	# max_heap to store the closest k stars seen so far.
	max_heap = []

	for star in stars:
		# add each star to the max_heap. If the max_heap size exceeds k, remove the maximum element
		# from the max heap
		# as python has only min heap, insert tuple (negative of distance, star)
		# to sort in reversed distance order.

		heapq.heappush(max_heap, (-star.distance, star))
		if len(max_heap) == k + 1:
			heapq.heappop(max_heap)

	# iteratively extract from max-heap, which yeilds the stars sorted according from furthest to
	# closest.
	return[s[1] for s in heapq.nlargest(k, max_heap)]


# space = O(k), time = O(nlogk)