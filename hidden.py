user_first = input("Guess the hidden 3 numbers from 3 attempts. For start push ENTER: ")
x = 26
y = 30
z = 50
first_input = input("Input first number: ")
first_input = int(first_input)
print(first_input == x or first_input == y or first_input == z)
second_input = input("Input second number: ")
second_input = int(second_input)
print(second_input == x or second_input == y or second_input == z)
third_input = input("Input third number: ")
third_input = int(third_input)
print(third_input == x or third_input == y or third_input == z)