charlotte = 183
tampa = 220	
pittsburgh = 422
los_angeles = 475

def hotel_cost(nights, hotel):
	if hotel == "Charlotte" or "charlotte":
		return nights * charlotte
	elif hotel == "Tampa" or "tampa":
		return nights * tampa
	elif hotel == "Pittsburgh" or "pittsburgh":
		return nights * nights_amount * pittsburgh
	elif hotel == "Los Angeles" or "los angeles":
		return nights * los_angeles
	else:
		print("You entered wrong information.")

hotel = input("Enter the name of the hotel: ")
nights = int(input("Enter the amount of the nights: "))

print(hotel_cost(nights, hotel))