# Test_for_cyclicity

'''
write a program that takes the head of a singly linked list and returns null if there does not exist
cycle, and the node at the start of the cycle, if cycle is present. (you do not know the length of
the list in advance.)

Hint: consider using two iterators, one fast, one slow.
'''

'''
in each iteration, advance the slow iterator by one and the fast iterator by two. 
the list has a cycle iff  the two iterators meet.
the reaoning is as follows: if the fast iterator jumps over te slow iterator, the slow iterator
will equal the fast iterator in the next step.

we can find the start of the cycle by first calculating the cycle length C.
once we know the cycle,and we have a node on it, it is trivial to compute a cycle length.
to find the firat node on the cycle, we use two iterators, one of which is C ahead of the other.
we advance them in tandem, and when they meet, that node must be the first node on the cycle.
'''

def has_cycle(head):
	def cycle_len(end):
		start = end
		step = 0
		while True:
			step += 1
			start = start.next
			if start is end:
				return step

	fast = slow = head

	while fast and fast.next and fast.next.next:
		slow = slow.next
		fast = fast.next.next

		if slow is fast:
			# finds the start of the cycle
			cycle_len_advanced_iter = head
			for _ in range(cycle_len(slow)):
				cycle_len_advanced_iter = cycle_len_advanced_iter.next

			it = head
			# both iterators advance in tandem
			while it is not cycle_len_advanced_iter:
				it = it.next
				cycle_len_advanced_iter = cycle_len_advanced_iter.next

			return it # iter is the start of the cycle.

	return None # no cycle


# the following program computes the beginning of the cycle without computing length of the cycle

def has_cycle(head):
	fast = slow = head

	while fast and fast.next and fast.next.next:
		slow = slow.next
		fast = fast.next.next

		if slow is fast:
			# tries to find the start of the cycle.

			slow = head
			# both pointers advance at the same time
			while slow is not fast:
				slow = slow.next
				fast = fast.next

			return slow # slow is the start of the cycle
	return None # no cycle.




