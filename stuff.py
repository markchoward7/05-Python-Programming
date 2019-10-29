def first_program():
    # Declare and initialize variables
    name = "Mark"
    address = "San Antonio, TX 78245"
    phone = "630-777-6374"
    afsc = "3D0X4"
    # Print out the info using fstring
    print(f"Name: {name}\nAddress: {address}\nPhone Number: {phone}\nAFSC: {afsc}")

first_program()

def second_program():
    # Prompt the user
    print("Enter total sales")
    # Calculate the profit at 1.23 * sales and display to user
    print("Profit from these sales: ${:.2f}".format(float(input()) * 1.23))

second_program()

def third_program():
    # Prompt the user
    print("Enter the square footage")
    # Calculate the acreage at 1/43560 sq feet and display to user
    print("The acreage of that amount: %.2f" % (float(input()) / 43560))

third_program()

def fourth_program():
    # Set price accumulator
    price = 0.0
    # Loop to get 5 price inputs from user and add them to accumulator
    for _ in range(5):
        print("Enter the price")
        price += float(input())
    # Calculate and display all the information
    print("Subtotal: $%.2f" % price)
    tax = price * 0.06
    print("Tax: $%.2f" % tax)
    print ("Total: $%.2f" % (price+tax))

fourth_program()

def fifth_program():
    # Does this one really need comments? Just read it
    speed = 60
    print(f"Distance at 5 hours: {speed*5}\nDistance at 8 hours: {speed*8}\nDistance at 12 hours: {speed*12}")

fifth_program()

def sixth_program():
    # Prompt the user for a price
    print("Enter the purchase price")
    price = float(input())
    # Calculate the taxes
    state_tax = price * 0.04
    county_tax = price * 0.02
    # Display all the information
    print("Price: $%.2f\nState Sales Tax: $%.2f\nCounty Sales Tax: $%.2f\nTotal Sales Tax: $%.2f\nTotal Cost: $%.2f" % (
            price, state_tax, county_tax, state_tax+county_tax, price+state_tax+county_tax))

sixth_program()

def seventh_program():
    # Prompt the user for miles and gallons
    print("Enter miles driven")
    miles = float(input())
    print("Enter gallons of gas used")
    gallons = float(input())
    # Display the calculated MPG
    print("{:.1f} MPG".format(miles/gallons))

seventh_program()

def eigth_program():
    # Prompt the user for a price
    print("Enter the amount of the meal")
    price = float(input())
    # Calculate the tip and tax
    tip = price * 0.15
    tax = price * 0.07
    # Display the information, including the calculated total
    print(f"Price: ${price:.2f}\nTip: ${tip:.2f}\nTax: ${tax:.2f}\nTotal: ${(price+tax+tip):.2f}")

eigth_program()

def ninth_program():
    # Prompt the user for a celsius temp
    print("Enter a temperature in Celsius")
    celsius = float(input())
    # Convert to fahrenheit and display
    print("That temperature in Fahrenheit is: %.1f" % (1.8*celsius + 32))

ninth_program()

def tenth_program():
    # Initialize variables with info given
    num_of_stock = 1000
    purchase_price = 32.87
    sale_price = 33.92

    # Do the basic calculations
    purchase_amount = num_of_stock * purchase_price
    sale_amount = num_of_stock * sale_price
    purchase_commission = purchase_amount * 0.02
    sale_commission = sale_amount * 0.02

    # Display the results
    print("Purchase amount: $%.2f" % (purchase_amount))
    print("Purchase commission: $%.2f" % purchase_commission)
    print("Sell amount: $%.2f" % (sale_amount))
    print("Sale commission: $%.2f" % sale_commission)
    # Calculate and display the final result
    print("Money Remaining: $%.2f" % (sale_amount - purchase_amount - purchase_commission - sale_commission))

tenth_program()