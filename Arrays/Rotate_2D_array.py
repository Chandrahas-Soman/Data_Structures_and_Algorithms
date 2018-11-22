# Rotate_a_2D_array

'''
Image rotation is fundamental operation in computer graphics.

1,2,3         90 degrees        7,4,1
4,5,6   -->   Clockwise   -->   8,5,2
7,8,9         rotation          9,6,3

write a function that takes input as an n*n 2D array, rotates the array by 90 degrees clockwise.

hint: focus on boundary elemnts
'''

''' brute force --> first row of original matrix is the last column of rotated.
       allocate a new n*n 2D array write the rotation to it(writing rows of the original matrix into
       columns of new matrix)

       time = O(n^2)
       space = O(n^2)
'''

'''
in place rotation. space = O(1)

we can perform rotation in a layer by layer fasshion- different layers can be processed independently
Furthermore, within a layer, we can exchange gropus of 4 elements at a time to perform the rotation.
e.g. send 1 to 4's, 4 to 16's, 16 to 13's and 13 to 1's then send 2 to 8's, 8 to 15's and so on.
'''

def rotate_matrix(square_matrix):
	matrix_size = len(square_matrix) - 1
	for i in range(len(square_matrix) // 2):
		for j in range(i, matrix_size - i):
			# perform 4 way exchange.
			# note that A[~i] for i in [0, len(A) - 1] is A[-(i + 1)]

			temp = square_matrix[i][j]
			square_matrix[i][j] = square_matrix[~j][i]
			square_matrix[~j][i] = square_matrix[~i][~j]
			square_matrix[~i][~j] = square_matrix[j][~i]
			square_matrix[j][~i] = temp

			print(square_matrix)
		print()
	print(square_matrix)

square_matrix = [[1,2,3,4],
				 [5,6,7,8],
				 [9,10,11,12],
				 [13,14,15,16]]

rotate_matrix(square_matrix)

# print(square_matrix[~0][~0]) # ---> square_matrix[3][3]
# print(square_matrix[~1][~1]) # ---> square_matrix[2][2]