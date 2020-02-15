limit = int(input("Limit: "))
odd = "ODD"
even = "EVEN"

def showNumbers(limit):
	for i in range(0, limit + 1):
		if i % 2 == 0:
			print(i, even)
		else:
			print(i, odd)

print(showNumbers(limit))