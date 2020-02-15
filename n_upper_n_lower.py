user_input = input("Enter some text: ")
n_upper = 0
n_lower = 0

def func1(n_upper, n_lower):

	for i in user_input:
		if i.isupper():
			n_upper += 1
	print(n_upper)
	
	for j in user_input:
		if j.islower():
			n_lower += 1
	print(n_lower)

func1(n_upper, n_lower)