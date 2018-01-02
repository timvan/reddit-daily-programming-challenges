# Rock Paper Scissors
# Project 1 Python
# 02-10-2015  20:14

from random import randint
import os

replay = "y"
score = [0,0] #(Human, Computer)

def input_maker():

	human = raw_input("Rock, Paper, Scissors...\nHuman throws:" ) 
	
	choice = ["Rock", "Paper", "Scissors"]

	comp_rnd = randint(0,2)

	computer = choice[comp_rnd]
	print "Computer throws: %s" %computer
	return (computer, human)


def decision_machine(computer, human):

	win_txt = "You Win!"
	loose_txt = "Computer Wins"
	
	if computer == human:
		result = 0
		print "Draw"
	elif computer == "Rock" and human == "Paper":
		result = 1
		print win_txt
	elif computer == "Rock" and human == "Scissors":
		result = -1
		print loose_txt
	elif computer == "Paper" and human == "Scissors":
		result = 1
		print win_txt
	elif computer == "Paper" and human == "Rock":
		result = -1
		print loose_txt
	elif computer == "Scissors" and human == "Rock":
		result = 1
		print win_txt
	elif computer == "Scissors" and human == "Paper":
		result = -1
		print loose_txt
	else: 
		print "Error!"
	
	return result


while replay == "y":
	
	(computer, human) = input_maker()
	
	result = decision_machine (computer, human)	

	replay = raw_input("Again? (y/n): ")
	os.system('clear')
	
	if result > 0:
		score[0] += 1
	elif result < 0:
		score[1] += 1
	else:
		score=score
	
print "Final score- Human: %d Computer: %d"	% (score[0],score[1])
print "Goodbye!"

		