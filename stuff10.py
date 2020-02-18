import os, pickle

import stuff10classes

def program_1():
    print("Enter the Production Worker's name")
    name = input()
    print("Enter the Production Worker's number")
    number = input()
    print("Enter the Production Worker's shift")
    shift = input()
    print("Enter the Production Worker's pay rate")
    pay = input()
    worker = stuff10classes.ProductionWorker(name, number, shift, pay)

    print("Name:", worker.get_name())
    print("Number:", worker.get_number())
    print("Shift:", worker.get_shift())
    print("Pay:", worker.get_pay())

def program_2():
    print("Enter the Shift Supervisor's name")
    name = input()
    print("Enter the Shift Supervisor's number")
    number = input()
    print("Enter the Shift Supervisor's salary")
    salary = input()
    print("Enter the Shift Supervisor's bonus")
    bonus = input()
    supervisor = stuff10classes.ShiftSupervisor(name, number, salary, bonus)

    print("Name:", supervisor.get_name())
    print("Number:", supervisor.get_number())
    print("Salary:", supervisor.get_salary())
    print("Bonus:", supervisor.get_bonus())

def program_3():

    def main():
        # call the load customers to get our database
        customers = load_customers()
        # welcome message
        print("Welcome to the customer database.")
        print("What would you like to do?")
        # while loop menu
        while True:
            print("\n[L]ook up a customer by name or number")
            print("[A]dd a customer entry")
            print("[E]dit a customer entry")
            print("[D]elete a customer entry")
            print("[V]iew entire mailing list")
            print("[Q]uit")
            # get the input and call the corresponding functions
            command = input().upper()
            if command == 'L':
                look_up(customers)
            elif command == 'A':
                customers = add(customers)
            elif command == 'E':
                customers = edit(customers)
            elif command == 'D':
                customers = delete(customers)
            elif command == 'V':
                view(customers)
            elif command == 'Q':
                # save data before quitting
                save_data(customers)
                quit()
            else:
                # invalid entry, loop again
                print("Invalid entry, try again")
    
    def load_customers():
    # function to load the customers dictionary from customers.dat using pickle
    # returns an empty dictionary if the file doesn't exist
        file_path = 'customers.dat'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                return pickle.load(file)
        else:
            return {}
    
    def save_data(customers):
    # function to save the dictionary of customers to customers.dat using pickle
        with open('customers.dat', 'wb') as file:
            pickle.dump(customers, file)

    def look_up(customers):
    # function to allow user to lookup customer info using name or number
    # using name returns all matching customers
    # using number returns only the matching number
        command = 0
        while command == 0:
            print("1 to look up by name, 2 by number, 3 to quit")
            try:
                command = int(input())
                if command == 1:
                    print("Enter the name to look up")
                    # get name input, then initialize list to store matches
                    name = input()
                    found = []
                    # loop through the values in the customers dictionary looking for matching names and add them to the list
                    for cust in customers.values():
                        if cust.get_name() == name:
                            found.append(cust)
                    # print any matching customers if found
                    if len(found) > 0:
                        print(found)
                    else:
                        # else print nothing found
                        print("No one found with name", name)
                elif command == 2:
                    print("Enter the number to look up")
                    # get number input
                    number = input()
                    # check if the number is in the customers dictionary
                    # then either print the matching entry or nothing found
                    if number in customers:
                        print(customers[number])
                    else:
                        print("No one found with number", number)
                # return on quit
                elif command == 3:
                    return
                else:
                    # invalid entry, loop again
                    print("Invalid entry, try again.")
                    command = 0
            except ValueError:
                # invalid entry, loop again
                print("Invalid entry, try again.")

    def add(customers):
    # function to add a customer entry
        print("Enter the customer number")
        cust_num = input()
        # make sure the customer number isn't already in use
        if cust_num in customers:
            print("Number already in use, please try again.")
            customers = add(customers)
            return customers
        else:
            # get all the inputs
            print("Enter the customer's name")
            name = input()
            print("Enter the customer's street address")
            street_address = input()
            print("Enter the customer's city")
            city = input()
            print("Enter the customer's state")
            state = input()
            print("Enter the customer's zip code")
            zip_code = input()
            print("Enter the customer's phone number")
            phone = input()
            # input check for mailing list
            print("Does the customer want to be on the mailing list? (y/n)")
            if input().lower() == 'y':
                on_mailing_list = True
            else:
                on_mailing_list = False
            # create an instance of the customer
            cust = stuff10classes.Customer(name, street_address, city, state, zip_code, phone, cust_num, on_mailing_list)
            # display the data and ask if everything looks correct before adding it to the dictionary
            print(cust)
            print("Is this accurate? (y/n)")
            if input().lower() == 'y':
                customers[cust_num] = cust
                print("Entry added")
            else:
                customers = add(customers)
        return customers
    
    def edit(customers):
        # function to edit customer entry
        cust_num = ''
        # while loop for input
        while cust_num == '':
            print("Enter the customer number, or q to quit")
            cust_num = input()
            # break the loop on q
            if cust_num == 'q':
                break
            # if the entry is not in the dictionary, state as such
            if cust_num not in customers:
                print("No record found for customer number", cust_num)
                cust_num = ''
            else:
                # print the info found and then ask for inputs
                # any blank entries result in copying the old information
                print(customers[cust_num])
                print("Enter the new name, or leave it blank to keep it the same.")
                name = input()
                if name == '':
                    name = customers[cust_num].get_name()
                print("Enter the new street address, or leave it blank to keep it the same.")
                street_address = input()
                if street_address == '':
                    street_address = customers[cust_num].get_street_address()
                print("Enter the new city, or leave it blank to keep it the same.")
                city = input()
                if city == '':
                    city = customers[cust_num].get_city()
                print("Enter the new state, or leave it blank to keep it the same.")
                state = input()
                if state == '':
                    state = customers[cust_num].get_state()
                print("Enter the new zip code, or leave it blank to keep it the same.")
                zip_code = input()
                if zip_code == '':
                    zip_code = customers[cust_num].get_zip_code()
                print("Enter the new phone number, or leave it blank to keep it the same.")
                phone = input()
                if phone == '':
                    phone = customers[cust_num].get_phone()
                # input check for mailing list
                print("Does the customer want to be on the mailing list? (y/n)")
                if input().lower() == 'y':
                    on_mailing_list = True
                else:
                    on_mailing_list = False
                # create an instance of the class
                cust = stuff10classes.Customer(name, street_address, city, state, zip_code, phone, cust_num, on_mailing_list)
                # show the new instance and ask the user to check for accuracy, if good then update the dictionary
                print(cust)
                print("Is this accurate? (y/n)")
                if input().lower() == 'y':
                    customers[cust_num] = cust
                    print("Entry updated")
                cust_num = ''
        return customers
    
    def delete(customers):
    # function to delete a customer entry
        print("Enter a customer number to delete")
        cust_num = input()
        # check if the entered num is in the dictionary
        if cust_num in customers:
            print(customers[cust_num])
            print("Are you sure you want to delete this entry? (y/n)")
            # check if they are sure they want to delete, if so then delete
            if input() == 'y':
                del customers[cust_num]
                print("Entry deleted")
        else:
            print("Entry not found")
        return customers
    
    def view(customers):
    # function to return the maililng address of all entries that are on the mailing list
        for cust in customers.values():
            if cust.get_on_mailing_list():
                print(cust.get_mailing_address())

    main()

program_3()