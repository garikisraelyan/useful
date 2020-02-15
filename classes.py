class Person:
	def __init__(self, name, surname, age, eye_color, hair_color):
		self.name = name
		self.surname = surname
		self.age = age
		self.eye_color = eye_color
		self.hair_color = hair_color

	def name_surname(self):
		return self.name + " " + self.surname

my_person = Person("Garik", "Israelyan", 17, "Brown", "Brown")

print(my_person.name)
print(my_person.hair_color)

print(my_person.name_surname())

my_person1 = Person("Nara", "Movsisyan", 18, "Green", "Shaten")

print(my_person1.name)
print(my_person1.hair_color)

print(my_person1.name_surname())