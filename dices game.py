d1 = int(input("Enter the number from the first dice: "))
d2 = int(input("Enter the number from the second dice: "))
sum_d = d1 + d2

if d1>=1 and d1<=6 and d2>=1 and d2<=6:
	if sum_d == 7 or sum_d == 11:
		print("You Won!")
	elif sum_d == 2 or sum_d == 3 or sum_d == 12:
		print("You Lost!")
	else:
		print(sum_d)
else:
	print("You didn't enter the numbers from the dice.")