class Pow:
	def __init__(self, number, power):
		self.number = number
		self.power = power

	def count_pow(self):
		j = 1
		for i in range(0, self.power):
			j *= self.number
		return j

user_input = Pow (int(input("Enter some number: ")), int(input("Enter the power of your number: ")))

print(user_input.count_pow())
