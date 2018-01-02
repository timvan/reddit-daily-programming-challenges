'''
Daily programmer challenges - reddit - 9.11.15

https://www.reddit.com/r/dailyprogrammer/comments/3s4nyq/20151109_challenge_240_easy_typoglycemia/
 
Given a paragraph return the paragraph where for each word, excluding the first and last letter,
the word is jumbled/shuffled

'''


import random

def typoglycemia(para):
	
	para_new=[]
	
	for word in para.split(" "):
		
		new_word = ""
		
		if len(word) > 3:
		
			punc = 0
			letters= list(word)
			
			if letters[-1] in ("?.,:;!-[]{}()""'"):
				punc = 1
			
			new_word = list(letters[0])	
			new_word += (random.sample(letters[1: -1 - punc], len(letters) - 2 - punc))
			new_word += letters[-1 - punc]
			
			if punc == 1:
				new_word += letters[-1]
			
			new_word = "".join(new_word)
			
		else:
			new_word = word
			
		para_new.append(str(new_word))
		
	para_new = " ".join(para_new)
	
	print(para_new)
		
		
			
				
def start():
	
	print "Welcome to the Typoglycemia creator!"
	#input_para = raw_input("Input a Paragraph: ")
	
	x = str("According to a research team at Cambridge University, it doesn't matter in what \
order the letters in a word are, the only important thing is that the first and last letter be in the right place. \
The rest can be a total mess and you can still read it without a problem. \
This is because the human mind does not read every letter by itself, but the word as a whole. \
Such a condition is appropriately called Typoglycemia.")
		
	input_para = x
		
	typoglycemia(input_para)
	
start()