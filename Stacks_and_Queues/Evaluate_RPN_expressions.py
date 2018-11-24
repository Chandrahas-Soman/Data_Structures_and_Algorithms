# Evaluate_RPN_expressions

'''
a string is said to be an arithmatic expression in reverse pollish notation (RPN) if:
i) it is a single digit or sequence of digits,prefixed with an option-,e.g.,'6','123','-21'
ii) it is one of the form "A,B,x" where A and B are RPN expressions and x is one of +,-,*,/.

An RPN expression can be evaluated uniquely to an integer, which is determined recursively.
The base case corresponds to rule1, which is integer expressed in base 10 positional system. Rule2 
corresponds to the recursive case, and the RPNs are evaluated in the natural way, e.g., if A evaluates
to 2 and B evaluates to 3, then "A,B,*" evaluates to 6.

write a program that takes an arithmatic expression in RPN and returns the number that the expression
evaluates to.

Hint: process subexpressions, keeping values in a stack. How should operators be handled?
'''

'''
we need to record results as we encounter operators, we apply them to partial results.
the partial results are added and removed in last in first out order, which makes a stack the 
natural data structure for evaluating RPN expreession.
'''

def evaluate(expression):
	intermediate_results = []
	delimiter = ','
	operators = {'+': lambda y,x: x+y,
					'-': lambda y,x: x-y,
					'*': lambda y,x: x*y,
					'/': lambda y,x: int(x/y)}

	for token in expression.split(delimiter):
		if token in operators:
			intermediate_results.append(operators[token](intermediate_results.pop(),
				intermediate_results.pop()))
		else: # token is a number
			intermediate_results.append(int(token))

	return intermediate_results[-1]

# O(1) computation per character of the string, the time complexity is O(n), where n is the length
# of the string.