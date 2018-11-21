# Buy_and_sell_a_stock_twice

'''
The max difference problem (previous) formalizes the maximum profit tat can be made by buying and 
then selling a single share over a given day range.

write a program that computes the maximum profit that can be made by buying and selling a share 
at most twice. The second buy must be made on another date after the first sale.

Hint: what do you need to know about the first i elements when processing the i+1 th element.
'''

'''
brute force buy-sell-buy-sell --> O(n^4)

elegant solution

but lets record into 2 lists. we record the best solution for A[0,j] where j between 1 and n-1
inclusive. and second we can perform reverse iterations, computing the best solution for single
buy singe sell for A[j, n-1], where j between 1 and n-1, inclusive. 

for each day we combine this result with the result from forward iteration for the previous day. 
This yeilds the maximum profit if we buy and sell once before
the current day and once at or after the current day.

M[i] = F[i-1] + B[i] 
'''

def buy_and_sell_stock_twice(prices):
	max_total_profit, min_price_so_far = 0.0, float('inf')
	first_buy_sell_profits = [0] * len(prices)

	# forward phase
	# for each day, we record max profit if we sell on that day

	for i, price in enumerate(prices):
		min_price_so_far = min(min_price_so_far, price)
		max_total_profit = max(max_total_profit, price - min_price_so_far)
		first_buy_sell_profits[i] = max_total_profit

	# backward phase
	# For each day, find the maximum profit if we make the seond buy on that day

	max_price_so_far = float('-inf')

	for i, price in reversed(list(enumerate(prices[1:], 1))):
		max_price_so_far = max(max_price_so_far,price)
		max_total_profit = max(max_total_profit, 
			max_price_so_far - price + first_buy_sell_profits[i-1])

	print(max_total_profit) 


a = [12,11,13,9,12,8,14,13,15]

buy_and_sell_stock_twice(a)
