# Advancing_through_an_array

'''
In a particular board game , aplayer has to try advance through a sequence of positions.
Each position has a nonnegative integer associated with it, representing the maximum you 
can advance from that position in one move.
You begin at the first postion, and win by getting to the last position.

e.g. let A = [3,3,1,0,2,0,1] represent the borad game. i.e. ith entry in A is the maximum 
we can advance from i. Then the game can be won by following sequence of advances from A:
take 1 step from A[0] to A[1]. (A[0] = 3 >= 1) => valid move
then take 3 steps from A[1] to A[4].
then take 2 steps from A[4] to A[6], which is the last position.

if A = [3,2,0,0,2,0,1] => game can't be won.

write a program which takes an array of n integers, A[i] denotes maximum you can advance
from index i, and returns whether it is possible to advance to the last index from the beginning
of the array.
'''

''' pseudo code

advancing as far as possible doesn't work as it may skip indices containing large entities.

we have to itereate through all entries in A. 
as we iterate through the array, we track the furthest index we know we can advance to.

if for some i before the end of the array, i is the furthest index that we have demonstrated
that we can advace to, we can not reach the last element. Otherwise, we can reach the end.
'''

# beautiful solution
def can_reach_end(A):
	furthest_reach_so_far, last_index = 0, len(A) - 1
	i = 0

	while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
		print(furthest_reach_so_far, A[i]+i)
		furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
		i += 1

	return furthest_reach_so_far >= last_index


a = [3,3,1,0,2,0,1]
b = [3,2,0,0,2,0,1]
c = [0,0,0,2]
print(can_reach_end(a))