
def main():
	print("\nWelcome to the integral calculator by addition.")
	print("Please input a calculation and hit enter")
	str_input = raw_input(">:")
	
	if not check_inputs(str_input):
		return
	
	a, op, b = str_input.split()
	int_a, int_b = int(a), int(b)
	
	
	print operators[op](int_a, int_b)
	
def check_inputs(inpt):
	str = inpt.split()
	
	if len(str) != 3:
		print "Error: not 3 inputs"
		return False
	if str[1] not in operators:
		print "Error: unknown operator"
		return False
	
	return True

def add(int_a, int_b):
	return int_a + int_b

def sub(int_a, int_b):
	total = 0
	incr = 1
	
	if int_b > int_a:
		incr = -1
		int_a, int_b = int_b, int_a
	
	while int_b < int_a:
		total += incr
		int_b += 1
		
	return total

def mult(int_a, int_b):
	total = 0
	
	if int_b < 0:
		int_b = sub(0, int_b)
		int_a = sub(0, int_a)
	
	for i in range(int_b):
		total += int_a
		
	return total
	
	
def dev(int_a, int_b):
	if int_b == 0:
		return "Error: deviding by zero"

	negative = False
	
	if int_a < 0 or int_b < 0:
		if not int_a < 0 and int_b < 0:
			negative = True 
	
	if int_b < 0:
		int_b = sub(0, int_b)
	if int_a < 0:
		int_a = sub(0, int_a)
			
	total = 0
	cnt = 0
	
	while total != int_a:
		total += int_b
		cnt += 1
		
		if total > int_a:
			return "Error: non-integral answer"
			break
		
	if negative:
		return sub(0, cnt)
	else:
		return cnt

def exp(int_a, int_b):
	total = 1
	
	if int_b < 0:
		return "Error: non-integral answer"
	
	for i in range(int_b):
		total = mult(total, int_a)
	
	return total

operators = {
	"+" : add,
	"-" : sub,
	"*" : mult,
	"/" : dev,
	"^" : exp,
	}

main()