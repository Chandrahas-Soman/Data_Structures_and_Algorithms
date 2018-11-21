def even_odd(a):

	next_even, next_odd = 0, len(a) - 1

	while next_even < next_odd:

		if a[next_even] % 2 == 0:
			next_even += 1

		else:
			a[next_even], a[next_odd] = a[next_odd], a[next_even]
			next_odd -= 1

		print(a)


a = [0,1,2,3,4,5,6,7]

# even_odd(a)

# b = [1] + [0] * 10
# b.append(42)

# b.remove(0)
# b.insert(3,28)
# print(len(b))
# print(b)


# deep copy shallow copy

b = [1,2,3]
c = b

# print(b)
# print(c)

# b.append(3)

# print(b)
# print(c)

d = [4,5,6]
e = list(d)

# print(d)
# print(e)

# d.append(7)

# print(d)
# print(e)


# reverse and reversed()

print(d.reverse())
print(d)
f = reversed(b)
print(f)
