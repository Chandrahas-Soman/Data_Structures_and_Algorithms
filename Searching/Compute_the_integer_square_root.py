# Compute_the_integer_square_root

'''
write a program which takes a nonnegative integer and returns the largest integer whose square is less
than or equal to the given integer.
e.g. if integer is 16, return 4. If integer is 300, return 17, since 17^2 = 289 < 300
Hint: Look out for a corner case.
'''

'''
if x^2 < k, then no number smaller than x can be the result, and if x^2 > k, then no number greater than
equal to x can be the result.
we initialize the interval to [0,k]. We compare the square of m = floor((l+r)/2) with k, and use the
elimination rule to update the inteval. If m^2 < k, we know all integers less than or equal to m 
have a square less than or equal to k. Therefore, we update the interval to [m+1,r]. If m^2 > k, we
know all numbers greater than or equal to m have a square greater than k, so we update the candidate
interval to [l, m-1]. The algorithm terminates when the interval is empty, in which case every number

e.g. if k=21, we initialize the interval to [0,21]. The mid point m = (floor(0+21)/2) = 10; since
10^2 = 100 > 21, we update the interval to [0,9]. now m = (0+9)/2 = 4 since 4^2= 16 < 21, we update
the interval to [5,9]. Now m = (5+9)/2 = 7, 7^2 > 21 => interval = [5,6] => 5^2 > 21 => [5,4] break. 
'''

def square_root(k):
	left, right = 0, k
	# candidate interval [left,right] where everythingbefore left has suqare <= k,
	# everything after right has > k
	while left <= right:
		mid = (left + right)//2
		mid_squared = mid * mid
		if mid_squared <= k:
			left = mid + 1
		else:
			right = mid + 1
	return left -1

# time = O(log n)