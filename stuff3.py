def program_1():
    
    def main():
        print("Enter an amount of kilometers")
        kilometers = float(input())
        output(kilometers)

    def output(kilos):
        print("That equals %.1f miles" % (kilos * 0.6214))
    
    main()

def program_3():

    def main():
        print("Enter the value of the property")
        value = float(input())
        output(value)

    def output(amount):
        print("Minimum insurance is $%.2f" % (amount * 0.8))

    main()

def program_4():

    def main():
        print("Enter monthly loan payment")
        loan = float(input())
        print("Enter monthly insurance payment")
        insurance = float(input())
        print("Enter monthly gas cost")
        gas = float(input())
        print("Enter monthly oil cost")
        oil = float(input())
        print("Enter monthly tire cost")
        tires = float(input())
        print("Enter monthly maintenance cost")
        mx = float(input())

        output([loan, insurance, gas, oil, tires, mx])

    def output(costs):
        total = 0
        for cost in costs:
            total += cost
        print("Total monthly cost: $%.2f\nAnnual Cost: $%.2f" % (total, (total*12)))
    
    main()

def program_5():

    def main():
        print("Enter the value of the property")
        value = float(input())

        output(value)
    
    def output(value):
        assessment = value * 0.6
        tax = assessment * 0.0064
        print("This value would be assessed at $%.2f and the tax would be $%.2f" % (assessment, tax))

    main()

def program_6():

    def main():
        print("Enter the individual's weight")
        weight = float(input())
        print("Enter the individual's height")
        height = float(input())

        output(weight, height)

    def output(weight, height):
        print("This person's BMI is %.1f" % (weight * 703 / height**2))

    main()

def program_7():

    def main():
        print("Enter the grams of fat")
        fat = float(input())
        print("Enter the grams of carbs")
        carbs = float(input())

        output(fat, carbs)

    def output(fat, carbs):
        print("Total calories: %.1f" % (fat*9 + carbs*4))

    main()

def program_8():

    def main():
        print("How many Class A tickets sold?")
        ticketsA = int(input())
        print("How many Class B tickets sold?")
        ticketsB = int(input())
        print("How many Class C tickets sold?")
        ticketsC = int(input())

        output(ticketsA, ticketsB, ticketsC)

    def output(ticketsA, ticketsB, ticketsC):
        total = ticketsA*15 + ticketsB*12 + ticketsC*9
        print("Income: $%d" % total)

    main()

def program_9():

    def main():
        print("Enter the square footage of wall space")
        area = float(input())
        print("Enter the cost of a gallon of paint")
        paint_cost = float(input())

        output(area, paint_cost)

    def output(area, paint_cost):
        gallons = area / 115
        hours = gallons * 8
        if hours > int(hours):
            labor_cost = (int(hours)+1) * 20
        else:
            labor_cost = hours * 20
        if gallons > int(gallons):
            gallons = int(gallons) + 1
        else:
            gallons *= int(gallons)
        paint_cost *= gallons
        print("Gallons required: %.1f" % gallons)
        print("Hours required: %.1f" % (hours))
        print("Paint cost: $%.2f" % (paint_cost))
        print("Labor charges: $%.2f" % (labor_cost))
        print("Total cost: $%.2f" % (paint_cost + labor_cost))

    main()

def program_10():

    def main():
        print("Enter total sales for the month")
        sales = float(input())

        output(sales)

    def output(sales):
        county_tax = sales * 0.02
        state_tax = sales * 0.04

        print("County Tax: $%.2f" % county_tax)
        print("State Tax: $%.2f" % state_tax)
        print("Total Tax: $%.2f" % (county_tax + state_tax))

    main()