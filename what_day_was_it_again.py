"""
[2017-10-30] Challenge #338 [Easy] What day was it again?

https://www.reddit.com/r/dailyprogrammer/comments/79npf9/20171030_challenge_338_easy_what_day_was_it_again/

Calculate the day of the week from a date

"""

def main():
	pass

	# inpt_str = input("Input data in format(YYYY MM DD): " ).split()
	inpt_str = ('0010 01 1').split()

	for i, x in enumerate(inpt_str):
		inpt_str[i] = int(x)

	if check_input(inpt_str):
		print (what_day_of_week(inpt_str))

def what_day_of_week(date):
	day = day_of_week[calc_num_days(date) % 7]
	return day

def calc_num_days(date):

	total = calc_initial_num_days(date) + calc_leap_days(date)
	print('days: ' + str(total))
	return total


def calc_leap_days(date):
	"""
	calculate the number of leap days to date
	leap-year if year is divisible by 4
	not leap-year if year is divisible by 100
	ignore leap-year last rule if year is divisible by 400
	"""
	leap_days = 0
	i = date[0]
	print (i)
	cond1 = i // 4
	cond2 = i // 100
	cond3 = i // 400
	
	leap_days = cond1 - cond2 + cond3 

	if i % 4 == 0:
	# if year is leap-year but before feb 28, minus one leap day
		if date[1] <= 2 and date[2] < 28:
			leap_days -= 1
			print ('yes')

	print ('leap_days: ' + str(leap_days))
	return leap_days


def calc_initial_num_days(date):
	# calculates the number of days to the date, exlcuding leap days

	total = (date[0] - 1) * 365 + days_till_first_of_mnth(date[1]) + (date[2] - 1)
	return total


def days_till_first_of_mnth(month):
	# calculates the number of days to the firt day of the month in the date

	total = 0
	last = 0
	days_till_first_of_month = {}

	for n in range(month - 1):
		total += days_in_month[n + 1]

	return total


def check_input(inpt_str):
	"""
	checks user input date is in correct format
	correct format: YYYYY MM DD
	
	and:

	8000 > YEAR > 0
	13 > MONTH > 0
	32 > DATE > 0

	"""

	if len(inpt_str) != 3:
		print ('Invalid Input: Date should have three integers')
		return False

	elif inpt_str[0] <= 0 or inpt_str[0] >= 8000:
		print ('Invalid Input: Year is not within 0 and 8000')
		return False

	elif inpt_str[1] <= 0 or inpt_str[1] >= 13:
		print ('Invalid Input: Month is not within 0 and 13')
		return False

	elif inpt_str[2] <= 0 or inpt_str[2] >= 32:
		print ('Invalid Input: Day is not within 0 and 32')
		return False

	else:
		return True

day_of_week = {
	2 : 'Monday',
	3 : 'Tuesday',
	4 : 'Wednesday',
	5 : 'Thursday',
	6 : 'Friday',
	0 : 'Saturday',
	1 : 'Sunday'

}

days_in_month = {
	1 : 31,
	2 : 28,
	3 : 31,
	4 : 30,
	5 : 31,
	6 : 30,
	7 : 31,
	8 : 31,
	9 : 30,
	10 : 31,
	11 : 30,
	12 : 31
}

if __name__ == "__main__":
	main()