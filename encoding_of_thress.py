# Game of Threes 9.11.15
# https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

'''
If the number is divisible by 3, divide it by 3.
If it's not, either add 1 or subtract 1 (to make it divisible by 3), then divide it by 3.
The game stops when you reach "1".
'''

import random

def game_of_threes(start_number):

	num = start_number
	steps = []

	while num > 1:
		
		if num % 3 == 0:
			print str(num) + "  0"
			num = num / 3
			steps.append(0)
		elif (num + 1) % 3 == 0:
			print str(num) + " 1"
			num = (num + 1) / 3
			steps.append(1)
		elif (num - 1) % 3 == 0:
			print str(num) + " -1"
			num = (num - 1) / 3
			steps.append(-1)
	# print steps
	print "1"
	
def start():
	
	print "Welcome to game of threes!"
	#start_number = raw_input("Starting Number: ")
	start_number = 999
	game_of_threes(start_number)
	

start()