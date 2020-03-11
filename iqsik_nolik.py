import random

player1 = input("Enter the name of Player 1: ")
player2 = input("Enter the name of Player 2: ")
my_list = []

my_list.append(player1)
my_list.append(player2)
first_player = random.choice(my_list)

for i in my_list:
	if i != first_player:
		second_player = i

if first_player == player1:
	print(player1, "plays as 'X'.")
	print(player2, "plays as 'O'.")
else:
	print(player2, "plays as 'X'.")
	print(player1, "plays as 'O'.")

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def print_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])

print_board()

def checking():
	if board[0] == board[1] == board[2] != "-" or board[0] == board[3] == board[6] != "-" or board[0] == board[4] == board[8] != "-" or board[1] == board[4] == board[7] != "-" or board[2] == board[4] == board[6] != "-" or board[2] == board[5] == board[8] != "-" or board[3] == board[4] == board[5] != "-" or board[6] == board[7] == board[8] != "-":
		if board[0] == "X" or board[4] == "X" or board[8] == "X":
			print("Game over!")
			print_board()
			print(first_player + " won the Game!")
		elif board[0] == "O" or board[4] == "O" or board[8] == "O":
			print("Game over!")
			print_board()
			print(second_player + " won the game!")

while True:
	while True:
		try:
			x_player_pos = int(input("Enter the position of 'X', " + first_player + ": "))
			if board[x_player_pos - 1] == "-":
				board[x_player_pos - 1] = "X"
				print_board()
				break
			else:
				print("This position is occupied. ")
		except:
			print("Enter a valid position for 'X'. ")

	if board[0] == board[1] == board[2] != "-" or board[0] == board[3] == board[6] != "-" or board[0] == board[4] == board[8] != "-" or board[1] == board[4] == board[7] != "-" or board[2] == board[4] == board[6] != "-" or board[2] == board[5] == board[8] != "-" or board[3] == board[4] == board[5] != "-" or board[6] == board[7] == board[8] != "-":
		checking()
		break
	elif "-" not in board:
		print("Game over!")
		print_board()
		print("Draw!")
		break

	while True:
		try:
			o_player_pos = int(input("Enter the position of 'O', " + second_player + ": "))
			if board[o_player_pos - 1] == "-":
				board[o_player_pos - 1] = "O"
				print_board()
				break
			else:
				print("This position is occupied. ")
		except:
			print("Enter a valid position for 'O'. ")

	if board[0] == board[1] == board[2] != "-" or board[0] == board[3] == board[6] != "-" or board[0] == board[4] == board[8] != "-" or board[1] == board[4] == board[7] != "-" or board[2] == board[4] == board[6] != "-" or board[2] == board[5] == board[8] != "-" or board[3] == board[4] == board[5] != "-" or board[6] == board[7] == board[8] != "-":
		checking()
		break
	elif "-" not in board:
		print("Game over!")
		print_board()
		print("Draw!")
		break
