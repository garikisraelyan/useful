number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))


if number1 >= number2 and number1 > number3:
	if number1 == number2:
		print("Number 1 and Number 2: ", number1)
	else:
		print("Number 1: ", number1)

elif number2 > number1 and number2 >= number3:
	if number2 == number3:
		print("Number 2 and Number 3: ", number2)
	else:
		print("Number 2: ", number2)

elif number3 >= number1 and number3 > number2:
	if number3 == number1:
		print("Number 1 and Number 3: ", number3)
	else:
		print("Number 3: ", number3)

else:
	print("They're the same numbers.")
