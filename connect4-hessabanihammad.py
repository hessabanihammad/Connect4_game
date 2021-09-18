import random, os, time

#parameters 
numRows=6
numCols=7
board=[]
numPlayers=2
checkers=["X","O"]
turn=random.randint(0,numPlayers-1)
win = False
elapsedTurns=0

#functions
def PrintBoard():
	#printing the board
	os.system("clear") 
	for r in range(numRows):
		for c in range(numCols):
			print(board[r][c],end=" ")
		print()

#creating the board 
for r in range(numRows):
	tmp=[]
	for c in range(numCols):
		tmp.append("-")
	board.append(tmp)


def CheckWin():
	#horizontal location win, so we check the neighboring coloumns, if 4 in a row its a win 
	#subtracted 3 from the number of coloumns because only 4 coloumns can form a win from the total coloumns of the game
	for c in range(numCols-3):
		for r in range(numRows):
			if board[r][c]== checkers[turn] and board[r][c+1]==checkers[turn] and board[r][c+2]==checkers[turn] and board[r][c+3]==checkers[turn]:
				PrintBoard()
				print(checkers[turn],"won the game!")
				return True 
	#vertical win, so we check the neighboring rows 
	for c in range(numCols):
		for r in range(numRows-3):
			if board[r][c]==checkers[turn] and board[r+1][c]==checkers[turn] and board[r+2][c]==checkers[turn] and board[r+3][c]==checkers[turn]:
				PrintBoard()
				print(checkers[turn],"won the game!")
				return True 
	#diagonal I (positive slope) 
	for c in range(numCols-3):
		for r in range(numRows-3):
			if board[r][c]==checkers[turn] and board[r+1][c+1]==checkers[turn] and board[r+2][c+2]==checkers[turn] and board[r+3][c+3]==checkers[turn]:
				PrintBoard()
				print(checkers[turn],"won the game.")
				return True  

	#diagonal II (negatively sloped)
	for c in range(numCols-3):
		for r in range(3,numRows):
			if board[r][c]==checkers[turn] and board[r-1][c+1]==checkers[turn] and board[r-2][c+2]==checkers[turn] and board[r-3][c+3]==checkers[turn]:
				PrintBoard()
				print(checkers[turn],"won the game.")
				return True 
	#draw 
	if elapsedTurns==42:
		print("The game is a draw. None of you win!")
#this is the game loop which will loop until there's a winner or a draw is formed 
gameover=False 
while not gameover:
	PrintBoard()
	print("Welcome to Connect 4!")
	print("To win the game, one of the players needs to form a horizontal,vertical, or diagonal line of four checkers. If none of this is formed, the game is a draw.")
	#ask for player 1 or player 2 input (Randomly select the player)
	choice=input(checkers[turn] + " please choose a coloumn ")
	#error checking on user input 
	while not choice.isdigit() or int(choice) > 6:
		print("Wrong Input")
		choice=input(checkers[turn] + " please choose a coloumn ")
	row = numRows-1
	while row != -1:
		if board[row][int(choice)]=="-": #check if the spot is valid: empty spot
			board[row][int(choice)]=checkers[turn]
			elapsedTurns+=1
			gameover=CheckWin()
			break
		else:
			row -= 1
	turn=(turn+1)%numPlayers


