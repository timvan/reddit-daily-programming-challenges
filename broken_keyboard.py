"""
24.10.2015

https://www.reddit.com/r/dailyprogrammer/comments/3pcb3i/20151019_challenge_237_easy_broken_keyboard/

Help! My keyboard is broken, only a few keys work any more. 
If I tell you what keys work, can you tell me what words I can write?
You'll be given a line with a single integer on it, telling you how many lines to read. 
Then you'll be given that many lines, each line a list of letters representing the keys 
that work on my keyboard.

Example input:

3
abcd
qwer
hjklo

output:

abcd = bacaba
qwer = ewerer
hjklo = kolokolo

"""

import re

words_url = "/Users/Tim-Mac/temp/Reddit/english_words.txt"
WORDS = []

input_letters = "bnki"
#input_keys = []
#input_keys = list(input_letters)
last_max = []

for word in open(words_url).readlines():
	letters = list(word.replace("\n",""))
	#print word
	#print letters
	#print letters
	#print list(input_letters)
	match = re.match("^[" + input_letters + "]*$", word.replace("\n","").replace("\r",""))
	if match:
		if len(word) > len(last_max):
			last_max = word

print last_max
		
		
	
'''
def check_word(input_letters, word):
	pattern = "r'[^" + input_letters + "]'"
	prog = re.compile(pattern)
	result = prog.match(word)
	print result

print check_word("acbd", "acbd")

'''