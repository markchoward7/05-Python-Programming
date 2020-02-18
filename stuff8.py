import os
import pickle


file_path = r"directory.dat"

def main():
    # load data
    directory = load_data()
    # set the inputs to accept from the user
    available_commands = ['Lookup', 'Display', 'Add', 'Exit']
    # while loop to allow the user to keep working until they are done
    while True:
        # get the user's input
        print("What would you like to do?", available_commands)
        command = input().title()
        # while loop for validation
        while command not in available_commands:
            print("Command was not recognized, what would you like to do?", available_commands)
            command = input().title()
        # ifs to call the appropriate function based on input
        if command == "Lookup":
            directory = lookup(directory)
        elif command == "Display":
            display(directory)
        elif command == "Add":
            directory = add(directory)
        elif command == "Exit":
            save_data(directory)
            exit()


def load_data():
    # if the file exists, loads the dictionary from the binary file
    # returns that or a blank dictionary if no file exists
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    else:
        return {}

def save_data(directory):
    # save the data to a binary file
    with open(file_path, 'wb') as file:
        pickle.dump(directory, file)

def lookup(directory):
    # lookup function to allow the user to find a specific entry
    # get the user to enter a name to lookup
    print("Enter a name to lookup")
    name = input()
    # check if name is in directory
    if name not in directory:
        print("Name not found")
    else:
        # print the findings
        print(f"Name: {name}\nEmail: {directory[name]}")
        # ask the user if they want to edit
        print("Would you like to edit this email? (y/n)")
        if input().lower() == 'y':
            print("Enter a new email address. Or enter 'delete' to remove the entry.")
            command = input()
            # if user wants to delete, then delete the entry
            if command == "delete":
                del directory[name]
                print("Removed %s from directory." % name)
            else:
            # otherwise, update the entry
                directory[name] = command
                print("Updated %s with email %s." % (name, command))
    return directory

def display(directory):
    # function to display entire directory
    for name, address in directory.items():
        print(f"Name: {name}\nEmail: {address}")

def add(directory):
    # function to add a name to the directory
    # first get user input
    print("Enter the name of the person you want to add.")
    name = input()
    # if name is in dictionary, ask user if they want to update instead
    if name in directory:
        print("That person is already in the directory with the email of %s" % directory[name])
        print("Would you like to change this address? (y/n)")
        if input() == 'y':
            print("Enter a new email address.")
            address = input()
            directory[name] = address
            print("Updated %s with email address %s" % (name, address))
    else:
        # otherwise, prompt for an email and add the entry to the directory
        print("Enter an email address.")
        address = input()
        directory[name] = address
        print("Added %s with email address %s" % (name, address))
    return directory
main()