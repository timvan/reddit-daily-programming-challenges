# Multiplication Table

# Request two numbers and create the multiplication table of those numbers

def start():

	print ("Welcome to multiplication table emulator!")
	print ("Choose two numbers to create a multiplication table!")
	
	while True:
		N1 = raw_input("Number 1:")
		
		try:
			N1 += 1
		except TypeError:
		
		
		if not isinstance(N1 , (int, long))
			print('Error: Insert Whole Number')
		else:
			N2 = raw_input("Number 2:")
				
			if not isinstance( N2,(int,long))
				print('Error: Insert Whole Number')
			else:
				print("Here..")
				quit()

start()