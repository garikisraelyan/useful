'''my_list = ["wallet", "phone", '5935', '7891', "gag", "keys"]
n_of_str = 0
for i in my_list:
	if i[0] == i[-1]:
		n_of_str += 1
print(n_of_str)
user_input1 = input("Enter the first text: ")
user_input2 = input("Enter the next text: ")
if len(user_input1) == len(user_input2):
	print(user_input1[0:int(len(user_input1)/2)], user_input2[int(len(user_input2)/2):-1])
else:
	print("None.")
#result = 0
user_input = int(input("Enter a number: "))
for i in range(0, user_input):
	i += 1
	while user_input == i ** 2:
		print("Right.")
		break'''

fibonacci = [1, 2]
a = 0

while max(fibonacci) < 100:
	fibonacci_next = (fibonacci[a] + fibonacci[a + 1])
	fibonacci.append(fibonacci_next)
	a += 1
print(fibonacci)