def check_winner(board):
    size = len(board)

    for i in range(size):
        row = "".join(board[i])
        col = "".join(board[j][i] for j in range(size))
        if row == "X" * size or col == "X" * size:
            return "X"
        if row == "O" * size or col == "O" * size:
            return "O"

    diagonal1 = "".join(board[i][i] for i in range(size))
    diagonal2 = "".join(board[i][size - 1 - i] for i in range(size))

    if diagonal1 == "X" * size or diagonal2 == "X" * size:
        return "X"
    if diagonal1 == "O" * size or diagonal2 == "O" * size:
        return "O"

    return "Ничья"

board = []
first_row = input()
board.append(first_row)
for i in range(len(first_row) - 1):
    row = input()
    board.append(row)
result = check_winner(board)
print(result)