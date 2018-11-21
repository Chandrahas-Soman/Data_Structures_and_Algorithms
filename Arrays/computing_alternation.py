# computing_alternation

'''
write a program that takes an array A of numbers, and rearranges A's elements to get a new array B
having a property that B[0] <= B[1] => B[2] <= B[3] <= ..
'''

# hint: can you solve the problem by making local changes to A.

'''
solution1: straight forward solution is to sort A and interleave the bottom and top halves of sorted
array.

solution2: alternatively, we can sort array and swap the elements at the pairs (A[1],A[2]), 
(A[3],A[4]), ..

both of these approaches have same time complexity O(nlogn)
'''

'''
solution 3: its not necessary to sort A, we can simply rearrange the elements around the median,
and then perform the interleaving.

However, the desired ordering is very local.
Iterating through the array and swapping A[i] and A[i+1] when i is even and A[i] > A[i+1]
or i is odd and A[i] < A[i+1]
'''

def rearrange(A):
	for i in range(len(A)):
		A[i:i +2] = sorted(A[i:i+2], reverse=i % 2)

