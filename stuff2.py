def program_0():
    while True:
        print("Enter hourly payrate")
        try:
            payrate = float(input())
            break
        except:
            print("Payrate must be a number")
    while True:
        print("Enter hours worked")
        try:
            hours = float(input())
            if hours > 0:
                break
            else:
                print("Hours must be a positive number.")
        except:
            print("Hours must be a positive number.")
    if hours > 40:
        pay = 40*payrate + (hours - 40)*payrate*1.5
    else:
        pay = hours * payrate
    print("Gross pay: $%.2f" % pay)

def program_1():
    # While loop for input validation
    while True:
        print("Enter a whole number between 1 and 10")
        try:
            num = int(input())
            if num < 1 or num > 10:
                print("Number must be between 1 and 10")
            else:
                break
        except:
            print("A number is required")
    # if else to determine the roman numeral required, multiply some I's when you can to reduce total number of ifs
    if num == 10:
        roman = 'X'
    elif num == 9:
        roman = 'IX'
    elif num >= 5:
        roman = 'V' + 'I' * (num - 5)
    elif num == 4:
        roman = 'IV'
    else:
        roman = 'I' * num
    # Print the results
    print(f"That number in roman numerals is: {roman}")

def program_2():
    # Get some inputs, no validation
    print("Enter the length of the first rectangle")
    length1 = float(input())
    print("Enter the width of the first rectangle")
    width1 = float(input())
    print("Enter the length of the second rectangle")
    length2 = float(input())
    print("Enter the width of the second rectangle")
    width2 = float(input())
    # Calculate both the areas
    area1 = length1 * width1
    area2 = length2 * width2
    # Check which is larger and print the findings
    if area1 > area2:
        print("The first rectangle is larger")
    elif area2 > area1:
        print("The second rectangle is larger")
    else:
        print("The rectangles are of equal size")

def program_3():
    # Get input without validation
    print("Enter the object's mass")
    mass = float(input())
    # Calculate weight
    weight = mass * 9.8
    # If to check weight and print the findings
    if weight > 1000:
        print("Object is too heavy")
    elif weight < 10:
        print("Object is too light")
    else:
        print("The weight is %.1f newtons" % weight)

def program_4():
    # Get inputs without validation
    print("Enter a numeric month")
    month = int(input())
    print("Enter a numeric day")
    day = int(input())
    print("Enter a 2 digit year")
    year = int(input())
    # Calcualte and check for magic date and print the findings
    if month * day == year:
        print("This is a magic date")
    else:
        print("This is not a magic date")

def program_5():
    # List of primary colors for input validation
    PRIMARY_COLORS = ["RED", "BLUE", "YELLOW"]
    # Dictionary of color combinations, when primary color strings are combined they will need to be in alphabetical order
    COMBINATIONS = {"BLUERED" : "purple", "BLUEYELLOW" : "green", "REDYELLOW" : "orange"}
    # While for input validation
    while True:
        # Get input
        print("Enter a primary color")
        color1 = input().upper()
        # Check if input is in the list
        if color1 in PRIMARY_COLORS:
            # Get input
            print("Enter another primary color")
            color2 = input().upper()
            # Check if input is in the list
            if color2 in PRIMARY_COLORS:
                # Who is combining the same color together?
                if color1 == color2:
                    print("Those were the same color....try again")
                    continue
                # Check which color starts first alphabetically and then combine them into one string
                if color1 < color2:
                    combined = color1 + color2
                else:
                    combined = color2 + color1
                    # Print the results using the dictionary
                print("These colors combine to make {}".format(COMBINATIONS[combined]))
                break
            else:
                # Try again
                print("That is not a primary color, start over")
        else:
            # Try again
            print("That is not a primary color, start over")

def program_6():
    # Get inputs without validation
    print("Enter a number of pennies")
    pennies = int(input())
    print("Enter a number of nickels")
    nickels = int(input())
    print("Enter a number of dimes")
    dimes = int(input())
    print("Enter a number of quarters")
    quarters = int(input())
    # Calculate the amount
    amount = pennies + nickels*5 + dimes*10 + quarters*25
    # Check the amount and print the corresponding statement
    if amount == 100:
        print("Congratulations! You win!")
    elif amount > 100:
        print("That amount is greater than one dollar")
    else:
        print("That amount is less than one dollar")

def program_7():
    # Get input without validation
    print("Enter the number of books you purchased")
    books = int(input())
    # Check the books and award points
    if books >= 4:
        points = 60
    elif books == 3:
        points = 30
    elif books == 2:
        points = 15
    elif books == 1:
        points = 5
    else:
        points = 0
    # print the results
    print("You've earned %d points" % points)

def program_8():
    # Get input without validation
    print("Enter the number of packages purchased")
    packages = int(input())
    # Set cost and initialize discount
    cost = 99 * packages
    discount = 0.0
    # Check package amount and calculate discount accordingly
    if packages >= 100:
        discount = cost * 0.5
    elif packages >= 50:
        discount = cost * 0.4
    elif packages >= 20:
        discount = cost * 0.3
    elif packages >= 10:
        discount = cost * 0.2
    # Subtract discount to get the new cost
    cost -= discount
    # Print the results
    print("Your discount was worth $%.2f. Your total cost is $%.2f" % (discount, cost))

def program_9():
    # Get input without validation
    print("Enter the weight of the package")
    weight = float(input())
    # Check weight and calculate cost accordingly
    if weight > 10:
        cost = weight * 3.8
    elif weight > 6:
        cost = weight * 3.7
    elif weight > 2:
        cost = weight * 2.2
    else:
        cost = weight * 1.1
    # Print results
    print("The cost is $%.2f" % cost)

def program_10():
    # Get inputs without validation
    print("Enter the individual's weight")
    weight = float(input())
    print("Enter the individual's height")
    height = float(input())
    # Calculate bmi
    bmi = weight * 703 / height**2
    # Check bmi and print corresponding statement
    if bmi > 25:
        print("This person is overweight")
    elif bmi >= 18.5:
        print("This person's weight falls in the optimal range")
    else:
        print("This person is underweight")

def program_11():
    # Get input without validation
    print("Enter a number of seconds")
    seconds = int(input())
    # Check seconds and print corresponding statement with calculated results
    if seconds >= 86400:
        print("There are %.1f days in %d seconds" % (seconds / 86400, seconds))
    elif seconds >= 3600:
        print("There are %.1f hours in %d seconds" % (seconds / 3600, seconds))
    elif seconds >= 60:
        print("There are %.1f minutes in %d seconds" % (seconds / 60, seconds))
    else:
        print("That's not very long")

