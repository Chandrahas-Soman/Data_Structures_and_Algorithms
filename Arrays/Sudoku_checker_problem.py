# Sudoku_checker_problem

'''
Check whether a 9*9 2D array representing a partially completed sudoku is valid. Specifically check 
that no row, no column, no 3*3 2D subarray contains duplicates.A zero value in 2D array indicates that
entry is blank; every other entry is in [1,9].

Hint: directly test constraints. Use an array to encode sets.
'''
'''
solution : there is no real scope for algorithm optimization in this problem- its all about writing
a cleancode.!
'''
# check if partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
	# returns true if subarray partial_assignmetn[start_row:end_row][strat_col: end_col] contains
	# any duplicates in {1, 2, .. , len(partial_assignment)} otherwise return false.
	def has_duplicate(block):
		block = list(filter(lambda x: x != 0, block))
		return len(block) != len(set(block))

	n = len(partial_assignment)

	# check row and column constraints.
	if any (
		has_duplicate([partial_assignment[i][j] for j in range(n)])
		or has_duplicate([partial_assignment[j][i] for j in range(n)])
		for i in range(n)):
		return False

	# check region constraints
	region_size = int(math.sqrt(n))

	return all (not has_duplicate([
			partial_assignment[a][b]
			for a in range(region_size * I, region_size * (I + 1))
			for b in range(region_size * J, region_size * (J + 1))
		]) for I in range(region_size) for J in range(region_size))