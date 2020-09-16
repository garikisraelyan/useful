fibonacci = [1]
# j = 0

# for i in range(0, 9):
# 	j = fibonacci[i] + fibonacci[i - 1]
# 	fibonacci.append(j)

# print(fibonacci)


fibonacci = [1, 2]
i = 0

while True:
	i = fibonacci[-1] + fibonacci[-2]
	if i < 200:
		fibonacci.append(i)
	else:
		break

print(fibonacci)
