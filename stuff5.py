import os
import random

def program_1():
    # open the file and print the stuff
    with open('numbers.txt', 'r') as file:
        for line in file:
            print(line.strip())

def program_2():
    # get input and check if it exists
    print("Enter the name of the file")
    file_path = input()
    if os.path.exists(file_path):
        # open the file
        with open(file_path, 'r') as file:
            # read the first 5 lines, break if the line is blank
            for _ in range(5):
                text = file.readline().strip()
                if (text == ''):
                    break
                print(text)
    else:
        print("Could not find the file %s" % file_path)

def program_3():
    # get the input and check if it exists
    print("Enter the name of a file")
    file_path = input()
    if os.path.exists(file_path):
        # open the file
        with open(file_path, 'r') as file:
            # print the line number and the data with an enumerated loop
            for line_num, line in enumerate(file):
                print("%d: %s" % ((line_num+1), line))
    else:
        print("Could not find the file %s" % file_path)

def program_4():
    # open the file and get the linecount
    with open('names.txt', 'r') as file:
        print(len(file.readlines()))

def program_5():
    # open the file
    with open('numbers.txt', 'r') as file:
        # initialize an accumulator
        total = 0
        # loop through the file, adding to the accumulator
        for line in file:
            total += int(line.strip())
        # print the results
        print(total)

def program_6():
    # open the file
    with open('numbers.txt', 'r') as file:
        # initialize the accumulator
        total = 0
        # loop through the file, adding to the accumulator
        for line in file:
            total += int(line.strip())
        # go back to the start of the file
        file.seek(0)
        # calculate average using the linecount
        average = total / len(file.readlines())
        # print the results
        print(average)

def program_7():
    # while loop for input validation
    while True:
        print("Enter a number of random numbers to generate.")
        try:
            # set input to num
            num = int(input())
            # ensure it is positive
            if num > 0:
                break
            else:
                print("Number must be positive.")
        except:
            print("Must be a number.")
    # open the file
    with open('random_numbers.txt', 'w') as file:
        # loop to write a number of random numbers equal to the num input
        for _ in range(num):
            file.write(str(random.randint(1, 100)) +'\n')

def program_8():
    # open the file
    with open('random_numbers.txt', 'r') as file:
        # initialize an accumulator
        total = 0
        # add each line to the total
        for line in file:
            total += int(line.strip())
        # print the results
        print(total)
        # go back to the start of the file and get the linecount
        file.seek(0)
        print(len(file.readlines()))

def program_9():
    # try except to catch any problems opening the file
    try:
        program_6()
    except IOError:
        print("There was a problem opening the file")

def program_10():
    # write function
    def write():
        # remove old data
        os.remove('golf.txt')
        # while loop to get inputs, will break on -q
        while True:
            print("Enter the golfer's name, type -q to quit")
            name = input()
            if name == '-q':
                break
            else:
                # get score input as well
                print("Enter score for %s" % name)
                score = input()
                # write the data to the file
                with open('golf.txt', 'a') as file:
                    file.write(name + ":" + score + '\n')
    # read function
    def read():
        # open the file
        with open('golf.txt', 'r') as file:
            # iterate through the file
            for line in file:
                # split the data on the :
                data = line.split(':')
                # print out the results
                print('Name: %s\t Score: %s' % (data[0], data[1]))

    write()
    read()