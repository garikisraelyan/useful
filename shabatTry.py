'''a = input("Write something: ")
#b = input("Write something again: ")
def some_function(a):
	c = ""
	for i in a:
		result = i * 2
		c += result
	print(c)
some_function(a)'''

'''result = 0
for i in range(1, 1000):
	if i % 3 == 0 or i % 5 == 0:
		result += i
print(result)'''
'''
radius = int(input("Enter the radius: "))
height = int(input("Enter the height: "))
print("The volume of the cylinder is", 3.14*(radius**2)*height)'''

'''a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))
if c ** 2 == a ** 2 + b ** 2 or a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2:
	print("This is a right triangle.")
else:
	print("Your triangle is not right.")'''

'''for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

while True:
	try:
		user_input = int(input("Enter a number: "))
		break
	except:
		print("You did not enter a number.")