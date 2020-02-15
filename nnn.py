n = int(input("Enter a digit: "))

def final_number(n):
	if n > 9 or n < 0:
		print("You didn't enter a digit.")
	else:
		result = n * 111 + n * 11 + n
		return result

print(final_number(n))