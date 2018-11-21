# buy_and_sell_stock_once

'''

design an algorithm that determines the maximum profit that could have been made by buying and then 
selling a single share over a given day range, subject to the constraint that the buy and the sell 
have to take place at the start of the day.

e.g. stock prices = [310,315,275,295,260,270,290,230,255] --> max profit buy at 260 and sell at 290
(note that 260 is not the lowest price and 290 is not the highest price in the day range.)

write a program that takes an array denoting the daily stock price, and returns the maximum profit
that could be made by buying and then selling one share of that stock. There is no need to buy if 
no profit is possible.
'''

# hint: focus on valid difference

''' solution1
brute force algorithm would be appropriate. 

for each pair of indices i and j > i, if s[j] - s[i] is greater than the largest differnce seen so
far, update the largest differnce to s[j] - s[i].

time complexity --> O(n^2)
'''

''' solution 2
divide and conquer can be used to improve upon the brute force algorithm
split S into twosubarrays, S[0: n/2] and S[n/2 + 1, n-1] and compute the best reslut for the first 
and second subarrays and combine these results.

also need to consider the case where theoptimum buy and sell take place in different subarrays.

complexity = O(nlogn)

corner cases -->empty subarrays, subarray of length one, and an array in which price decreases 
monotonically.
'''

'''
solution 3

maximum profit that can be made by selling on a specific day is determined by minimum of stock prices
over the previous days. since maximum profit correspond to selling on some day.

iterate through S, keeping track of the minimum element m seem thus far.
if difference of current element and m is greater than maximum profit recordedso far, update
the maximum profit.

simpler than divide and conquer. 
'''

# so simple
def buy_and_sell_stock_once(prices):
	min_price_so_far, max_profit = float('inf'), 0.0

	for price in prices:
		max_profit_sell_today = price - min_price_so_far
		max_profit = max(max_profit, max_profit_sell_today)
		min_price_so_far = min(min_price_so_far, price)

	return max_profit