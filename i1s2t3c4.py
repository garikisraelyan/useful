user_input = input("Enter some text: ")
dic1 = {}

for i in user_input:
	dic1[i] = user_input.count(i)

print(dic1)