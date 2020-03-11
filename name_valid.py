user_name = input("Write some name: ")

def check(x):
	if x == x.title():
		names_list = x.split()
		if len(names_list) == 3:
			if (names_list[0][1] == "." and len(names_list[0]) == 2 and names_list[1][1] == "." and len(names_list[1]) == 2 or (len(names_list[0]) > 1 and "." not in names_list[0]) or (len(names_list[1]) > 1 and "." not in names_list[1])) and len(names_list[2]) > 1 and "." not in names_list[2]:
				return True
			else:
				return False
		elif len(names_list) == 2:
			if names_list[0][1] == "." and len(names_list[0]) == 2 or names_list[1][1] == "." and len(names_list[1]) == 2 or (len(names_list[0]) > 1 and "." not in names_list[0]) or (len(names_list[1]) > 1 and "." not in names_list[1]):
				return True
		else:
			return False
	else:
		return False

print(check(user_name))
