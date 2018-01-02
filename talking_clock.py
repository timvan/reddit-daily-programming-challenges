"""

[2017-06-27] Challenge #321 [Easy] Talking Clock 
https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/

Description:
No more hiding from your alarm clock! You've decided you want your computer to keep you updated on the time so you're never late again. A talking clock takes a 24-hour time and translates it into words.
Input:
An hour (0-23) followed by a colon followed by the minute (0-59).
Output:
The time in words, using 12-hour format followed by am or pm.

"""

import datetime

def main():
	
	"""
	for i in range(0, 23):
		for j in range(0, 59):
			input_time = str(i) + ":" + str(j) 
	"""
		
	input_time = input("What is the time in format [hh:mm]:  ")

	hrs, mins = input_time.split(":")

	hrs, mins = int(hrs), int(mins)

	output  = ["It's", str(), str(), str()] 
	output[1] = hours(hrs)
	output[2] = minutes(mins) 
	output[3] = am_pm(hrs)

	print (" ".join(output))


def hours(hrs):
	if hrs == 12:
		return "twelve"
	else:
		x = hrs % 12
		return num_words[x]
		
def minutes(mins):
	if mins == 0:
		return ""
	elif mins >= 10 and mins <= 19:
		return num_words[mins]
	elif mins % 10 == 0:
		x = mins // 10
		return tens_words[x]
	else:
		x = mins // 10
		y = mins % 10
		return tens_words[x] + " " + num_words[y]


def am_pm(hrs):
	if hrs // 12 == 1:
		return "pm"
	else:
		return "am"

num_words = {
	0 : "",
	1 : "one",
	2 : "two",
	3 : "three",
	4 : "four",
	5 : "five",
	6 : "six",
	7 : "seven",
	8 : "eight",
	9 : "nine",
	10 : "ten",
	11 : "eleven",
	12 : "twelve",
	13 : "thirteen",
	14 : "fourteen",
	15 : "fifteen",
	16 : "sixteen",
	17 : "seventeen",
	18 : "eighteen",
	19 : "nineteen"
	}
	

tens_words = {
	0 : "oh",
	2 : "twenty",
	3 : "thirty",
	4 : "fourty",
	5 : "fifty"
	}

main()