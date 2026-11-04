EMPTY = " "
ROOK = "R"
KNIGHT = "N"
PAWN = "P"

board = [[EMPTY for _ in range(8)] for _ in range(8)]

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

board[4][2] = KNIGHT

board[3][4] = PAWN

for row in board:
	print(" ".join(row))

