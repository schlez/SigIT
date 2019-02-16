winflag = False  # boolean flag to indicate a winning situation (will become True)


# the function gets a tic tac toe board and checks for winning or tie
def check_win(board):
    global winflag
    check_rows(board)
    if winflag:  # If a winner has been found the function will stop
        return None
    check_cols(board)
    if winflag:  # If a winner has been found the function will stop
        return None
    check_diagonals(board)
    if winflag:  # If a winner has been found the function will stop
        return None
    print("tie")  # In case that there is no winner


# check for winner in the rows
# The function will take sequence of 3 cells from the board and will check them in the check_seq function
def check_rows(board):
    global winflag
    for row in board:
        winflag = check_seq(row)
        if winflag:  # If a winner has been found the function will stop
            return None


# check for winner in the cols
# The function will take sequence of 3 cells from the board and will check them in the check_seq function
def check_cols(board):
    global winflag
    for i in range(len(board)):
        col = []  # In order to append a sequence of 3 cells
        for j in range(len(board)):
            col.append(board[j][i])
        winflag = check_seq(col)
        if winflag:  # If a winner has been found the function will stop
            return None


# check for winner in the main diagonal
# The function will take sequence of 3 cells from the board and will check them in the check_seq function
def check_diagonals(board):
    global winflag
    col = []
    for i in range(len(board)):
        col.append(board[i][i])
    winflag = check_seq(col)
    if winflag:  # If a winner has been found the function will stop
        return None

    # check for winner in the secondary diagonal
    col = []
    for i in range(len(board)):
        col.append(board[i][len(board) - i - 1])
    winflag = check_seq(col)
    if winflag:  # If a winner has been found the function will stop
        return None


# The function check if there is a sequence of 3 (1,1,1 OR 2,2,2) and will
# The function will print the winner (one or two) and return True if there is a sequence, else False
def check_seq(seq):
    count1, count2 = 0, 0
    for cell in seq:
        # count the phases of player 1
        if cell == 1:
            count1 += 1
        # count the phases of player 2
        if cell == 2:
            count2 += 1
            # In case there is a winner, print the name
    if count1 == 3 or count2 == 3:
        print("player 1 won") if count1 == 3 else print("player 2 won")
        return True  # to set the winning flag true


# The main function for the game board
def main():
    board = [[1, 2, 1],
             [2, 1, 2],
             [1, 2, 1]]
    check_win(board)  # check for winner


if __name__ == "__main__":
    main()
