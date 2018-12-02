# Is_an_anonymous_letter_constructible

'''
write a program that takes text for an anomymous letter and text for a magzine and determines if it
is possible to write the letter using the magzine. The anonymous letter can be written using the 
magzine if for each character in the anonymous letter, the number of times it appears in the 
anonymous letter is no more than the number of times it appears in the magzine.

hint: count the number of times distinct caracter appearing in the letter.
'''

def is_letter_constructible_from_magzine(letter_text, magzine_text):
	# compute the frequencis for all chars in the letter_text
	char_frquency_for_letter = collections.Counter(letter_text)

	# checks if characters in magzine_text can cover characters in char_frquency_for_letter
	for c in magzine_text:
		if c in char_frquency_for_letter:
			char_frquency_for_letter[c] -= 1
			if char_frquency_for_letter[c] == 0:
				del char_frquency_for_letter[c]
				if not char_frquency_for_letter:
					# All characters for letter_text are matched.
					return True

	# Empty char_frquency_for_letter means every char in letter_text can be covered by a character
	# in magzine text.
	return not char_frquency_for_letter


# Pythonic solution.
# in Counters, subtraction only keeps keys with positive counts.

def is_letter_constructible_from_magzine_pythonic(letter_text, magzine_text):
	return (not collections.Counter(letter_text) - collections.Counters(magzine_text))