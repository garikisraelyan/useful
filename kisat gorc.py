bank_account = 6000

user_inputed_price = int(input("Enter the price of the item: "))

if bank_account >= user_inputed_price:
	print("You can buy this item.")

elif bank_account < user_inputed_price:
	user_input_loan = input("You can't buy this item. Do you want a loan? ")
	if user_input_loan == "Yes" or "yes":
		inputed_loan = int(input("How much money do you want? "))
		if inputed_loan + bank_account >= user_inputed_price:
			print("Now you can buy this item!")

		else:
			print("You can't buy this item.")

else:
	print("You can't buy this item.")