user_temp = float(input("Enter the temperature: "))
user_input = input("Enter the type of the temperature (C, F or K): ")

if user_input == "C":
	print((user_temp)*1.8+32, "F")
	print((user_temp)+273, "K")

elif user_input == "F":
	print(((user_temp)-32)/1.8, "C")
	print(((user_temp)-32)/1.8+273, "K")

elif user_input == "K":
	print((user_temp)-273, "C")
	print(((user_temp)-273)*1.8+273, "F")

else:
	print("Enter the type of the temperature.")