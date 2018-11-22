# Compute_the_spiral_ordering

'''
1,2,3          Clockwise spiral ordering is
4,5,6   -->    1,2,3,6,9,8,7,4,5
7,8,9

write a program that takes n*n 2D array and returns spiral ordering of the array

hint: use case analysis and divide and conquer
'''

'''
uniformly addd boundary.

add n-1 elements of first row.
then add n-1 elements of last column.
then add n-1 elements of las row in reverse order.
and finally add the last n-1 elements of first column in reverse.

after this we are left with the problem of adding the elements of n-2 * n-2 2D array in spiral order
this leads to an iterative algorithm that adds the outermost elements of n*n, n-2*n-2, .. 2D arrays

(matrix of odd dimension has a corner case, when we reach its center.) 
'''

def matrix_in_spiral_order(square_matrix):
	def matrix_layer_in_clockwise(offset):
		if offset == len(square_matrix) - offset - 1:
			# square matrix has odd dimension, and we are at the center of the square matrix
			spiral_ordering.append(square_matrix[offset][offset])
			return

		spiral_ordering.extend(square_matrix[offset][offset: -1 - offset])
		spiral_ordering.extend(list(zip(*square_matrix))[-1 - offset][offset: -1 - offset])
		spiral_ordering.extend(square_matrix[-1 -offset][-1 - offset: offset: -1])
		spiral_ordering.extend(list(zip(*square_matrix))[offset][-1 -offset: offset: -1])

	spiral_ordering = []

	for offset in range(len(square_matrix)+1 // 2):
		matrix_layer_in_clockwise(offset)

	print(spiral_ordering)






square_matrix = [[1,2,3,4],
				 [5,6,7,8],
				 [9,10,11,12],
				 [13,14,15,16]]

matrix_in_spiral_order(square_matrix)

'''
for offset in range(len(square_matrix)+1 // 2):
	print(offset)
	print(square_matrix[offset][-1 -offset: offset: -1])
	#print(square_matrix[-1 - offset][offset: -1 - offset])
	#print(list(zip(*square_matrix)))
'''