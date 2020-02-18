def program_1():
    # Initialize accumulator
    total = 0
    # 7 iteration for loop, don't need the counter variable
    for _ in range (7):
        # While loop for input validation
        while True:
            print("Enter the number of bugs for the day.")
            try:
                # Add input to accumulator
                total += int(input())
                break
            except:
                print("That wasn't a number, try again.")
    # Print result
    print("The total number of bugs was %d." % total)

def program_2():
    # Loop starts at 10 and iterates every 5 where it ends at 30
    for minute in range (10, 31, 5):
        # Calculate and print the calories for that time
        print("Calories burned at minute %d: %.1f" % (minute, (minute * 3.9)))

def program_3():
    # while loop for input validation
    while True:
        print("Enter your monthly budget")
        try:
            # Set the initial budget
            budget = float(input())
            if (budget > 0):
                break
            else:
                print("Budget must be a positive number.")
        except:
            print("That wasn't a number, try again.")
    # dual while loops for input validation as well as check conditional break
    # If the break isn't used, the try except does validation
    # inner loop naturally exits on correct input, causing the else the else
    # the continue prevents hitting the break statement
    # breaking the inner loop with "q" input causes the else to be skipped and the outer loop to break
    while True:
        expense = 0.0
        while expense == 0.0:
            print("Enter an expense. Enter q to finish.")
            expense = input()
            if expense == "q":
                break
            try:
                expense = float(expense)
                budget -= expense
            except:
                print("That wasn't a number, try again.")
        else:
            continue
        break
    print("Your remaining budget is: $%.2f" % (budget))

def program_4():
    # while loop for input validation
    while True:
        print("Enter the speed of the vehicle.")
        try:
            # set speed to input
            speed = float(input())
            if speed > 0:
                break
            else:
                print("Speed must be a positive number.")
        except:
            print("Please enter a number.")
    # while loop for input validation
    while True:
        print("Enter the number of hours traveled.")
        try:
            # set hours to input
            hours = int(input())
            if hours > 0:
                break
            else:
                print("Time must be a positive number.")
        except:
            print("Please enter a number.")
    # for loop to calculate and display the outputs
    for hour in range(hours):
        print("Distance traveled at hour %d: %.0f" % (hour, hour * speed))

def program_5():
    # while loop for input validation
    while True:
        print("Enter the number of years.")
        try:
            # set the input to years
            years = int(input())
            if years > 0:
                break
            else:
                print("Years must be a positive number.")
        except:
            print("Please enter a number.")
    # initialize the accumulator
    total = 0
    # nested for loops for years and months
    for year in range(years):
        for month in range(12):
            # while loop for input validation
            while True:
                print("Enter the rainfall for year %d, month %d." % ((year + 1), (month + 1)))
                try:
                    # set input to rainfall
                    rainfall = float(input())
                    if rainfall >= 0:
                        total += rainfall
                        break
                    else:
                        print("Rainfall must be a positive number.")
                except:
                    print("Please enter a number.")
    # print and calculate the outputs
    print("The total rainfall was: %.1f" % total)
    print("The total months was: %d" % (years*12))
    print("The average rainfall per month was: %.1f" % (total / (years * 12)))

def program_6():
    # initialize and set the rows and columns
    rows = 3
    columns = 7
    # for loop for rows, set up a string accumulator inside this loop
    for row in range(rows):
        line = ""
        # inner for loop for columns, do all the calculations and then add the string to the line
        for col in range(columns):
            celsius = row*columns + col
            fahrenheit = celsius*1.8 + 32
            line += f"{celsius} C / {fahrenheit:.1f} F\t"
        # after the inner loop closes, print the line
        print(line)
            
def program_7():
    # while loop for input validation
    while True:
        print("Enter a number of days.")
        try:
            # set input to days
            days = int(input())
            if days > 1:
                break
            else:
                print("Days must be a positive number greater than 1.")
        except:
            print("Please enter a number.")
    # set columns, and then calculate how many rows are needed based on days
    columns = 5
    if days % columns == 0:
        rows = int(days / columns)
    else:
        rows = days // columns + 1
    # set initial salary and total pay
    salary = 0.01
    total = 0.01
    # for loop for rows, set a string accumulator here
    for row in range(rows):
        line = ""
        # for loop for columns, calculate everything and add the info to the string accumulator
        for col in range(columns):
            day = row*columns + col + 2
            if day <= days:
                salary *= 2
                total += salary
                line += f"D: {day}\tS: ${salary:.2f}\t\t"
        # after exiting the loop, print the line
        print(line)
    # print the total pay
    print("The total pay was $%.2f" % total)

def program_8():
    # initialize the accumulator
    total = 0
    # while loop for input validation and allow multiple netries
    while True:
        print("Enter a positive number, or a negative number to be done.")
        try:
            # set input to num
            num = int(input())
            # break loop on negative number
            if num < 0:
                break
            else:
                # accumulate
                total += num
        except:
            print("That wasn't a number")
    print("The sum of those numbers is %d" % total)

def program_9():
    # initialize and set rows and columns
    rows = 7
    columns = 7

    # for loop for rows, initialize a string accumulator here
    for row in range(rows):
        line = ""
        # for loop for columns, check if the column should have a star and add it to the accumulator
        for col in range(columns):
            if col < (rows - row):
                line += "*"
        # once outside the inner loop, print the line
        print(line)

def program_10():
    # initialize and set rows and columns
    rows = 6
    columns = 7

# for loop for rows, initialize a string accumulator here
    for row in range(rows):
        line = "#"
        # for loop for columns, check if column should have a space
        # if not, add a # and break the inner loop
        for col in range(1,columns):
            if col <= row:
                line += " "
            else:
                line += "#"
                break
        # once outside the inner loop, print the line
        print(line)

program_7()