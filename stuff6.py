import random

def program_1():
    sales_data = []
    while True:
        print("Enter the store's sales.")
        try:
            sales_data.append(float(input()))
            if len(sales_data) >= 7:
                break
        except ValueError:
            print("Sales must be a number.")
    total = 0
    for item in sales_data:
        total += item
    print("Total sales: $%.2f" % total)

def program_2():
    lotto = []
    for _ in range(7):
        lotto.append(random.randint(0,9))
    for item in lotto:
        print(item)

def program_3():
    rainfall = []
    while True:
        print("Enter the rainfall amount.")
        try:
            rainfall.append(float(input()))
            if len(rainfall) >= 12:
                break
        except:
            print("Rainfall must be a number.")
    total = 0
    for item in rainfall:
        total += item
    lowest = min(rainfall)
    highest = max(rainfall)
    print("Total rainfall: %.1f" % total)
    print("Average rainfall: %.1f" % (total / 12))
    print("Lowest month: %d" % (rainfall.index(lowest) + 1))
    print("Highest month: %d" % (rainfall.index(highest) + 1))

def program_4():
    numbers = []
    while True:
        print("Enter a number.")
        try:
            numbers.append(int(input()))
            if len(numbers) >= 20:
                break
        except:
            print("I said number.")
    total = 0
    for item in numbers:
        total += item
    print("Total: %d" % total)
    print("Average: %d" % (total / 20))
    print("Lowest: %d" % min(numbers))
    print("Highest: %d" % max(numbers))

def program_6():
    # Open the answerkey.txt file and set answer_key to it as a list
    with open("answerkey.txt", "r") as file:
        answer_key = list(file)
    # Open the answers.txt file and set answers to it as a list
    with open("answers.txt", "r") as file:
        answers = list(file)
    # Initialize an empty list for incorrect answers
    incorrect_answers = []
    # Enumerated loop to check answers and get the corresponding number
    for index, item in enumerate(answer_key):
        # If the answers do not match, add the index + 1 to the incorrect_answers list
        if item != answers[index]:
            incorrect_answers.append(index + 1)
    # Print the results
    if len(incorrect_answers) >= 6:
        print("You failed the exam.")
    else:
        print("You passed the exam.")
    print("You answered %d questions correctly." % (20 - len(incorrect_answers)))
    print("These were the questions you got wrong", incorrect_answers)

def program_7():
    # initialize the 2d list for the matrix
    matrix = [[],[],[],[]]
    # initalize lists for the highest rows and columns
    highestRow = [0]
    highestCol = []
    # for loop enumerating over the rows of matrix
    for index, row in enumerate(matrix):
        # initialize accumulator
        total = 0
        # for loop for 4 entries into each matrix row
        for _ in range(4):
            # generate a random number and add it to the matrix and to the accumulator
            randNum = random.randint(0,1)
            row.append(randNum)
            total += randNum
        # print the matrices
        print(row)
        # if not the first row
        if index != 0:
            # check if this row is bigger and replace the list if so
            if total > matrix[highestRow[0]].count(1):
                highestRow = [index]
            # otherwise, check if row is the same size and add it to list
            elif total == matrix[highestRow[0]].count(1):
                highestRow.append(index)
    # print highest row results
    print("Highest row(s):", highestRow)
    # initialize a list of accumulators for columns
    total = [0,0,0,0]
    # double range loop to get the matching indices for rows and columns
    for index in range(4):
        for index2 in range(4):
            # reverse the usage of indices to check columns instead of rows
            # and add to appropriate accumulator
            total[index] += matrix[index2][index]
    # for loop for the accumulators to check which ones are the highest
    for i in range(total.count(max(total))):
        highestCol.append(total.index(max(total)) + i)
        total.remove(max(total))
    # print results of highest column check
    print("Highest column(s):", highestCol)

# declared this outside program_8 definition due to scope issues
turn_count = 0
def program_8():
    # initialize and set the empty board
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

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

program_8()