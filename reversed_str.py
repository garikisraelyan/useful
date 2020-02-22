empty_string = " "

class SomeString:
	def __init__(self, my_string):
		self.my_string = my_string

	def reverse_str(self):
		my_list = self.my_string.split()
		reversed_list = my_list[-1::-1]
		return empty_string.join(reversed_list)

user_input = SomeString (input("Enter some text: "))

result = user_input.reverse_str()
print(result)
