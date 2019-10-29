while True:
    print ("Enter the cost of the item, enter -quit to quit")
    command = input()
    if command == "-quit":
        break
    else:
        try:
            cost = float(command)
            cost *= 1.07
            print ("$%.2f" % (cost))
        except:
            print("Value not accepted")