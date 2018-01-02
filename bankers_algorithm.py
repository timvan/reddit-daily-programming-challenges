"""
[2017-12-13] Challenge #344 [Intermediate] Banker's Algorithm
https://redd.it/7jkfu5

"""

import numpy as np

def main():

	
	a = get_bankers_list('bankers_algorithm_input.txt')

	(i, j, available, mx, allocation) = reshape_bankers_list(a)
	processes = list(range(i))

	if (allocation.sum(axis = 0) + available - mx.max(axis = 0)).min() < 0:
		print("Not enough resources")
		return

	order = []
	for m in range(i):

		if len(processes) == 0:
			break

		for n in processes:
			if check_is_less_or_equal(mx[n], available + allocation[n]):
				available += allocation[n]
				order.append(n)
				processes.remove(n)
				break


	if len(processes) > 0:
		print("No possible method")
	
	else:
		str_order = []
		for n in order:
			str_order.append("P" + str(n))
		print (" ".join(str_order))

def check_is_less_or_equal(array_1, array_2):
	for n in range(len(array_1)):
		if array_1[n] > array_2[n]:
			return False
	else:
		return True


def reshape_bankers_list(a):
	
	j = len(a[0]) 
	i = len(a) - 1

	available = np.array(a[0])
	mx = []
	allocation = []

	for n in range(i):
		mx.append(a[n+1][-j:])

	mx = np.array(mx)

	for n in range(i):
		allocation.append(a[n+1][:-j])

	allocation = np.array(allocation)

	return (i, j, available, mx, allocation)


def get_bankers_list(file_name):

	"""
	with open(file_name) as f:
		lines = f.readlines()
		print(lines)

	lines = [tuple(map(int, line.strip('[] \n\r').split())) for line in lines]
	print (lines)
	"""

	with open(file_name) as f:
		a = []
		for l in f:
			line = l.rstrip()
			if line:
				b = [int(i) for i in line.strip("[] ").split()]
				a.append(b)
	
	return a


if __name__ == "__main__":
	main()