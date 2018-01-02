"""
[2015-10-12] Challenge #236 [Easy] Random Bag System

Tetris piece chooser. A random piece is chosen from a bag of seven pieces and removed.
When the bg is empty, the bag is refreshed with the same seven pieces.
The pieces are O, I, S, Z, L, J, T

"""
import random

def tetris():

	pieces = ['O', 'I', 'S', 'Z', 'L', 'J', 'T']
	bag = []
	choice = []
	

	for num in range(7):
	
		bag = bag + pieces
	
		if len(bag)>0:
			while len(bag)>0:
				piece_pos=random.randrange(0, len(bag))
				choice.append(bag[piece_pos])
				del bag[piece_pos]
			
	print "".join(choice)
	print str(len(choice))

        
tetris()