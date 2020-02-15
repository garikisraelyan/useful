user_number = int(input("Enter a number: "))
fizz = "Fizz"
buzz = "Buzz"
FizzBuzz = "FizzBuzz"

def fizz_buzz (fizz, buzz, FizzBuzz):
	if user_number % 3 == False and user_number % 5 == True:
		return fizz
	elif user_number % 3 == True and user_number % 5 == False:
		return buzz
	elif user_number % 3 == False and user_number % 5 == False:
		return FizzBuzz
	else:
		return user_number

print(fizz_buzz(fizz, buzz, FizzBuzz))