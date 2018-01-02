# Game of Threes 9.11.15
# https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

'''
If the number is divisible by 3, divide it by 3.
If it's not, either add 1 or subtract 1 (to make it divisible by 3), then divide it by 3.
The game stops when you reach "1".
'''

import random

def game_of_threes(start_number, choice_values):

	num = start_number
	steps = []

	while num > 1:
		
		if num % 3 == 0:
			#print str(num) + "  0"
			num = num / 3
			steps.append(0)
		else:
			r = random.choice(choice_values)
			#print str(num) + "  " + str(r)
			num += r
			steps.append(r)
	
	if num != 1:
		steps = [1]
	
	return steps
			 
	
def zero_sum(start_number):
	
	choice_values = [-2, -1, 1, 1]
	
	steps = [1]
	
	while sum(steps) != 0:
		steps = game_of_threes(start_number, choice_values)
		
	print "success"
	print steps
	
	
def start():
	
	print "Welcome to game of threes!"
	#start_number = raw_input("Starting Number: ")
	start_number = 18446744073709551615
	zero_sum(start_number)
	

start()