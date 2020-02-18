# initialize and set the empty board
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
turn_count = 0

def main():
    # main function just starts the show
    print("Welcome to tic-tac-toe")
    display()

def choose():
    # Check whose turn it is to play
    if turn_count % 2 == 1:
        player = 'X'
    else:
        player = "O"
    print(player + "'s turn.")
    # while loop for input validation
    while True:
        print("Please select a row (1-3)")
        try:
            # Attempt to set input to row
            row = int(input())
            # Check if row is within range
            if row < 1 or row > 3:
                print("That is not a valid row, try again.")
            else:
                # Inner while loop for further input validation
                while True:
                    print("Please select a column (1-3)")
                    try:
                        # Attempt to set input to column
                        column = int(input())
                        # Check if column is within range
                        if column < 1 or column > 3:
                            print("That is not a valid column, try again.")
                        # Check if space has already been taken, if so break to start over at row selection
                        elif board[row - 1][column - 1] != ' ':
                            print("That space is unavailable. Please start over.")
                            break
                        else:
                            # This is where we end up if we get valid input
                            # Set the space to the player and then return
                            board[row - 1][column - 1] = player
                            return
                    except ValueError:
                        print("Please enter a number.")
        except ValueError:
            print("Please enter a number.")
        


def display():
# display function displays the current board state
# then calls check_end to see if the game continues
    for index, row in enumerate(board):
        row_string = ''
        for col in row:
            # add a | for formatting
            row_string += col + '|'
        # call strip to remove the last pipe
        print(row_string.strip('|'))
        # except on the last row, print this after the row for formatting
        if index < 2:
            print("-|-|-")
    check_end()

def check_end():
# The check_end function looks at all possible end state scenarios
# It calls upon the check_victory function with various string combos
# Then it checks if turn_count is at least 9 for a draw
# If it never hits, it won't return and then it will continue the game
    for row in board:
        row_string = ''
        for col in row:
            row_string += col
        if check_victory(row_string):
            print(f"{row_string[0]} wins")
            return
    for colIndex in range(3):
        col_string = ''
        for rowIndex in range(3):
            col_string += board[rowIndex][colIndex]
        if check_victory(col_string):
            print(f"{col_string[0]} wins")
            return
    if (check_victory(board[0][0] + board[1][1] + board[2][2])):
        print(f"{board[0][0]} wins")
        return
    if (check_victory(board[0][2] + board[1][1] + board[2][0])):
        print(f"{board[0][2]} wins")
        return
    global turn_count
    if turn_count >= 9:
        print("Cat's game")
        return
    turn_count += 1
    # Call choose first to get the player input
    # Choose will return when it gets good input, so then call display
    choose()
    display()

def check_victory(string_to_check):
# Simple function to see if either play has won the game with the string given
    if string_to_check == "XXX" or string_to_check == "OOO":
        return True
    return False

main()