import random

def program_1():
    # set up the dictionaries with the course info
    rooms = {'CS101' : '3004', 'CS102' : '4501', 'CS103' : '6755', 'NT110' : '1244', 'CM241' : '1411'}
    instructors = {'CS101' : 'Haynes', 'CS102' : 'Alvarado', 'CS103' : 'Rich', 'NT110' : 'Burke', 'CM241' : 'Lee'}
    times = {'CS101' : '8:00 a.m.', 'CS102' : '9:00 a.m.', 'CS103' : '10:00 a.m.', 'NT110' : '11:00 a.m.', 'CM241' : '1:00 p.m.'}
    # initialize course
    course = ''
    # while loop to ask for good input
    while course not in rooms:
        print("Enter a course number.")
        course = input()
    # print all the information on the requested course
    print('%s. Room: %s. Instructor: %s, Time: %s' % (course, rooms[course], instructors[course], times[course]))

def program_2():
    # torturous
    data = {'AL' : 'Montgomery', 'AK' : 'Juneau', 'AR' : 'Little Rock', 'AZ' : 'Phoenix', 'CA' : 'Sacramento',
            'CO' : 'Denver', 'CT' : 'Hartford', 'DE' : 'Dover', 'FL' : 'Tallahassee', 'GA' : 'Atlanta',
            'HI' : 'Honolulu', 'ID' : 'Boise', 'IL' : 'Springfield', 'IN' : 'Indianapolis', 'IA' : 'Des Moines',
            'KS' : 'Topeka', 'KY' : 'Frankfort', 'LA' : 'Baton Rouge', 'MA' : 'Boston', 'MD' : 'Annapolis',
            'ME' : 'Augusta', 'MI' : 'Lansing', 'MN' : 'Saint Paul', 'MO' : 'Jefferson City', 'MT' : 'Helena',
            'NC' : 'Raleigh', 'ND' : 'Bismarck', 'NE' : 'Lincoln', 'NH' : 'Concord', 'NJ' : 'Trenton',
            'NM' : 'Santa Fe', 'NV' : 'Carson City', 'NY' : 'Albany', 'OH' : 'Columbus', 'OK' : 'Oklahoma City',
            'OR' : 'Salem', 'PA' : 'Harrisburg', 'RI' : 'Providence', 'SC' : 'Columbia', 'SD' : 'Pierre',
            'TN' : 'Nashville', 'TX' : 'Austin', 'UT' : 'Salt Lake City', 'VA' : 'Richmond', 'VT' : 'Montpelier',
            'WA' : 'Olympia', 'WI' : 'Madison', 'WV' : 'Charleston', 'WY' : 'Cheyenne'}
    print("Welcome to the state capital quiz")
    # accumulators
    correct = 0
    total = 0
    # while loop to take input until user decides to be done
    while True:
        # add to total questions
        total += 1
        # pick a random state / capital pair
        state, capital = random.choice(list(data.items()))
        # ask the question
        print("What is the capital of %s" % state)
        # check the answer
        if input().title() == capital:
            # add to correct
            correct += 1
            print("That is correct")
        else:
            # give the correct answer if wrong
            print("That is incorrect, the correct answer was %s" % capital)
        # check if they want to go again
        print("Play again? (y/n)")
        if input().lower() != 'y':
            break
    # goodbye message
    print("Thank you for playing. You got %d correct out of %d questions." % (correct, total))

def program_3():
    # Jebus save me from this hell
    codes = {'A' : ',', 'a' : '.', 'B' : '/', 'b' : ';', 'C' : "'", 'c' : '[', 'D' : ']', 'd' : '`', 'E' : '1',
             'e' : '2', 'F' : '3', 'f' : '4', 'G' : '5', 'g' : '6', 'H' : '7', 'h' : '8', 'I' : '9', 'i' : '0',
             'J' : '<', 'j' : '>', 'K' : '?', 'k' : ':', 'L' : '"', 'l' : '{', 'M' : '}', 'm' : '~', 'N' : '!',
             'n' : '@', 'O' : '#', 'o' : '$', 'P' : '%', 'p' : '^', 'Q' : '&', 'q' : '*', 'R' : '(', 'r' : ')',
             'S' : '-', 's' : '=', 'T' : '_', 't' : '+', 'U' : 'e', 'u' : '|', 'V' : 'g', 'v' : 'E', 'W' : 'P',
             'w' : 'b', 'X' : 'H', 'x' : 'U', 'Y' : 'q', 'y' : 'f', 'Z' : 'M', 'z' : 'l'}
    # open the file and put the text in one long string
    with open('unencrypted.txt', 'r') as file:
        text = file.read()
    # string accumulator
    newText = ''
    # for each character in the text, add the corresponding code to the accumulator
    for char in text:
        newText += codes.get(char, ' ')
    # write the new text to a file
    with open('encrypted.txt', 'w') as file:
        file.write(newText)

def program_4():
    # open the file
    with open('uniquewords.txt', 'r') as file:
        # read the contents, replace the newlines with a space, then split the text on spaces and put in a set
        words = set(file.read().replace('\n', ' ').split(' '))
    # print the set
    print(words)

def program_5():
    # empty dictionary
    frequency = {}
    # open the file
    with open('uniquewords.txt', 'r') as file:
        # read the contents, replace the newlines with a space, then split the text on spaces
        words = file.read().replace('\n', ' ').split(' ')
    # loop through the words
    for word in words:
        # if it is in the dictionary, increment the value
        # otherwise add it to the dictionary at the value of 1
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    # print the results
    print(frequency)

def program_6():
    # open the first file
    with open('unencrypted.txt', 'r') as file:
        # read the contents, replace the newlines with a space, then split the text on spaces and put in a set
        words1 = set(file.read().replace('\n',' ').split(' '))
    # open the second file
    with open('uniquewords.txt', 'r') as file:
        # read the contents, replace the newlines with a space, then split the text on spaces and put in a set
        words2 = set(file.read().replace('\n', ' ').split(' '))

    # print all the combinations asked for using the or, xor, and - operators
    print("All unique words", (words1 | words2))
    print("In first file, but not second", (words1 - words2))
    print("In second file, but not first", (words2 - words1))
    print("Words that appear in either file, but not both", (words1 ^ words2))

program_6()