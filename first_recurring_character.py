"""
[2017-11-13] Challenge #340 [Easy] First Recurring Character

https://www.reddit.com/r/dailyprogrammer/comments/7cnqtw/20171113_challenge_340_easy_first_recurring/

Write a program that outputs the first recurring character in a string.

"""

def main():

	inpt_str = input('Input string: ')
	print(first_recurring_character_dict(inpt_str))
	print(first_recuring_character(inpt_str))



def first_recuring_character(inpt_str):
	"""Function takes input string of chracters, and returns 

	"""

	for index, char_i in enumerate(inpt_str):	
		for char_j in inpt_str[index + 1:]:
			if char_i == char_j:
				return ('Found first recurring character: ' + char_i +
					'\nOriginal character at position: ' + str(index + 1))

	return 'No recurring character found'


def first_recurring_character_dict(inpt_str):

	dt = {}

	for index, char in enumerate(inpt_str):
		if char in dt:
			return "Char: " + str(char) + "\nPosition: " + str(dt[char] + 1)
		else:
			dt[char] = index

	return 'No recurring character found'


	
main()