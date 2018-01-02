 
def main():
	str1 = input("str1: ")
	str2 = input("str2: ")
	check_permutation(str1, str2)

	print(check_permutation2(str1, str2))

def check_permutation(str1, str2):
	
	sorted_lst1 = sorted(list(str1.lower()))
	sorted_lst2 = sorted(list(str2.lower()))

	for i, c in enumerate(sorted_lst1):
		if sorted_lst2[i] != c:
			print ("not check_permutation")
			break
	else:
		print ("permutation")

def check_permutation2(str1, str2):
	
	sorted_lst1 = sorted(list(str1.lower()))
	sorted_lst2 = sorted(list(str2.lower()))

	if len(sorted_lst1) == len(sorted_lst2):
		return sorted_lst2 == sorted_lst1
	else:
		return False

if __name__ == "__main__":
	main()
