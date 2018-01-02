"""
[2017-10-09] Challenge #335 [Easy] Consecutive Distance Rating
https://www.reddit.com/r/dailyprogrammer/comments/759fha/20171009_challenge_335_easy_consecutive_distance/

Description
We'll call the consecutive distance rating of an integer sequence the sum of the distances between consecutive integers.
Consider the sequence 1 7 2 11 8 34 3. 1 and 2 are consecutive integers, but their distance apart in the sequence is 2.
2 and 3 are consecutive integers, and their distance is 4. The distance between 7 and 8 is 3. The sum of these distances is 9.
Your task is to find and display the consecutive distance rating of a number of integer sequences.

Input
You'll be given two integers a and b on the first line denoting the number of sequences that follow and the length of those sequences,
respectively. You'll then be given a integer sequences of length b, one per line. The integers will always be unique and range from 1 to 100 inclusive.

Output
Output each consecutive distance rating, one per line.
"""


    def main():
    
    	sentinel = ''
    	for input_line in iter(raw_input, sentinel):
    		input_ints = [int(n) for n in input_line.split()]
    		print consecutive_distance_rating_line(input_ints)
    
    def consecutive_distance_rating_line(str_nums):
    	# returns the consecutive rating of the line on numbers
    	rating = 0
    	new_str = str_nums
    	for n in str_nums[:-1]:
    		rating += consecutive_distance_rating_first(new_str)
    		new_str.remove(n)
    
    	return rating
    	
    
    def consecutive_distance_rating_first(str_nums):
    	# returns the consectuive distance rating of the first number in  a list
    	rating = 0
    	for i in range(len(str_nums)-1):
    		if str_nums[i+1] == str_nums[0] + 1 or str_nums[i+1] == str_nums[0] - 1:
    			rating += i + 1
    	return rating
    
    main()