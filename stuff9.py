import os, pickle, random, time

def program_1():

    class Pet:

        def __init__(self, name, animal, age):
            self._name = name
            self._animal = animal
            self._age = age

        def set_name(self, name):
            self._name = name
        def get_name(self):
            return self._name
        
        def set_animal(self, animal):
            self._animal = animal
        def get_animal(self):
            return self._animal
        
        def set_age(self, age):
            self._age = age
        def get_age(self):
            return self._age
    
    print("Enter your pet's name.")
    name = input()
    print("Enter the kind of animal it is.")
    animal = input()
    print("What is %s's age?" % name)
    age = input()

    your_pet = Pet(name, animal, age)
    print("Your %s named %s is %s" % (your_pet._animal, your_pet._name, your_pet._age))

def program_2():

    class Car:

        def __init__(self, year, model, make):
            self._year = year
            self._model = model
            self._make = make
            self._speed = 0
        
        def accelerate(self):
            self._speed += 5

        def brake(self):
            self._speed -= 5

        def get_speed(self):
            return self._speed
    
    my_car = Car(2010, "Corolla", "Toyota")
    my_car.accelerate()
    print(my_car.get_speed())
    my_car.accelerate()
    print(my_car.get_speed())
    my_car.accelerate()
    print(my_car.get_speed())
    my_car.accelerate()
    print(my_car.get_speed())
    my_car.accelerate()
    print(my_car.get_speed())
    my_car.brake()
    print(my_car.get_speed())
    my_car.brake()
    print(my_car.get_speed())
    my_car.brake()
    print(my_car.get_speed())
    my_car.brake()
    print(my_car.get_speed())
    my_car.brake()
    print(my_car.get_speed())

def program_3():

    class Info:

        def __init__(self, name, address, age, phone):
            self._name = name
            self._address = address
            self._age = age
            self._phone = phone
        
        def set_name(self, name):
            self._name = name
        def get_name(self):
            return self._name

        def set_address(self, address):
            self._address = address
        def get_address(self):
            return self._address
        
        def set_age(self, age):
            self._age = age
        def get_age(self):
            return self._age
        
        def set_phone(self, phone):
            self._phone = phone
        def get_phone(self):
            return self._phone

    person1 = Info("Fake Person 1", "123 Fake Street", "55", "555-5555")
    person2 = Info("Fake Person 2", "234 Real Street", "44", "444-4444")
    person3 = Info("Fake Person 3", "345 Unkown Street", "1000000", "1")

def program_4():

    class Employee:

        def __init__(self, name, id_num, department, job_title):
            self._name = name
            self._id_num = id_num
            self._department = department
            self._job_title = job_title
        
        def __str__(self):
            return "%s\t%s\t\t%s\t%s" % (self._name, self._id_num, self._department, self._job_title)
    
    susan = Employee("Susan Meyers", "47899", "Accounting", "Vice President")
    mark = Employee("Mark Jones", "39119", "IT        ", "Programmer")
    joy = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

    print("Name\t\tId Number\tDepartment\tJob Title")
    print(susan)
    print(mark)
    print(joy)

def program_5():

    class RetailItem:

        def __init__(self, description, inventory, price):
            self._description = description
            self._inventory = inventory
            self._price = price

        def __str__(self):
            return "%s\t%d\t\t\t$%.2f" % (self._description, self._inventory, self._price)

    item1 = RetailItem("Jacket    ", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt    ", 20, 24.95)

    print("Description\tUnits in Inventory\tPrice")
    print(item1)
    print(item2)
    print(item3)

class Employee:

        def __init__(self, name, id_num, department, job_title):
            self._name = name
            self._id_num = id_num
            self._department = department
            self._job_title = job_title

        def set_name(self, name):
            self._name = name
        def set_id(self, id_num):
            self._id_num = id_num
        def set_department(self, department):
            self._department = department
        def set_job_title(self, job_title):
            self._job_title = job_title

        def __str__(self):
            return "%s\t%s\t\t%s\t%s" % (self._name, self._id_num, self._department, self._job_title)

def program_6():

    def load_employees():
        file_path = 'employee_data.dat'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                return pickle.load(file)
        else:
            return {}

    def main_menu(employees):
        print("Welcome to the Employee Management System")
        print("What would you like to do?")
        available_commands = ['l', 'a', 'c', 'd', 'q']
        command = ''
        while command not in available_commands:
            print("[L]ook up an employee")
            print("[A]dd a new employee")
            print("[C]hange an existing employee's information")
            print("[D]elete an employee")
            print("[Q]uit")
            command = input().lower()
            if command not in available_commands:
                print("Unrecognized command, please try again.")
        if command == 'l':
            lookup(employees)
        elif command == 'a':
            add(employees)
        elif command == 'c':
            change(employees)
        elif command == 'd':
            delete(employees)
        elif command == 'q':
            with open('employee_data.dat', 'wb') as file:
                pickle.dump(employees, file)
            exit()
    
    def lookup(employees):
        print("Enter the name of the employee you are looking for.")
        name = input()
        if name in employees:
            print(employees[name])
        else:
            print("Could not find %s" % name)
        main_menu(employees)

    def add(employees):
        print("Enter the name of the employee to add")
        name = input()
        if name in employees:
            print("%s is already in the employee dictionary")
        else:
            print("Enter %s's ID number." % name)
            id_num = input()
            print("Enter %s's department." % name)
            department = input()
            print("Enter %s's job title." % name)
            job_title = input()
            employees[name] = Employee(name, id_num, department, job_title)
            print("Successfully added %s with the following info:" % name)
            print(employees[name])
        main_menu(employees)

    def change(employees):
        print("Enter the name of the employee you want to edit.")
        name = input()
        if name in employees:
            print("This is the current information on file for %s" % name)
            print(employees[name])
            print("Enter %s's name." % name)
            name = input()
            print("Enter %s's ID number." % name)
            id_num = input()
            print("Enter %s's department." % name)
            department = input()
            print("Enter %s's job title." % name)
            job_title = input()
            employees[name] = Employee(name, id_num, department, job_title)
            print("Successfully changed %s to the following:" % name)
            print(employees[name])
        else:
            print("Could not find %s" % name)
        main_menu(employees)

    def delete(employees):
        print("Enter the name of the employee you want to delete.")
        name = input()
        if name in employees:
            del employees[name]
            print("Successfully deleted %s" % name)
        else:
            print("Could not find %s" % name)
        main_menu(employees)

    employees = load_employees()
    main_menu(employees)

def program_7():
    
    class RetailItem:

        def __init__(self, description, inventory, price):
            self._description = description
            self._inventory = inventory
            self._price = price

        def get_price(self):
            return self._price
        def __str__(self):
            return "%s\t$%.2f" % (self._description, self._price)

    class CashRegister:

        def __init__(self, items=[]):
            self._items = items

        def purchase_item(self, item):
            self._items.append(item)

        def get_total(self):
            total = 0
            for item in self._items:
                total += item.get_price()
            return total

        def show_items(self):
            print("Description\tPrice")
            for item in self._items:
                print(item)

        def clear(self):
            self._items.clear()

    item1 = RetailItem("Jacket    ", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt    ", 20, 24.95)

    register = CashRegister([item1, item2, item3])
    register.show_items()
    print(register.get_total())
    register.clear()

    register.purchase_item(item1)
    register.purchase_item(item1)
    register.purchase_item(item3)
    register.show_items()
    print(register.get_total())

def program_8():

    class Question:
    # class for questions, contains the question itself, all of its possible answers,
    # the correct answer, and a bit of extra information to be displayed afterwards
        def __init__(self, question, answers, correct_answer, extra_trivia):
            self._question = question
            self._answers = answers
            self._correct_answer = correct_answer
            self._extra_trivia = extra_trivia
        # the getters used by the application
        def get_question(self):
            return self._question
        def get_answers(self):
            return self._answers
        def get_extra_trivia(self):
            return self._extra_trivia
        # checks to see if supplied answer is the same as the correct answer and returns true/false
        def check_answer(self, answer):
            if answer == self._correct_answer:
                return True
            else:
                return False
        # shuffles the list of answers
        def shuffle_answers(self):
            random.shuffle(self._answers)

    def main():
        # welcome message
        print("Welcome to trivia.")
        time.sleep(1)
        print("This game is for 2 people to compete")
        time.sleep(1)
        print("Each player will take turns answering questions")
        time.sleep(1)
        print("Whoever gets the most right out of 5 wins")
        time.sleep(1)
        print("Ready or not, the game is about to start...")
        time.sleep(3)
        # load the questions from the file using load_questions
        questions = load_questions()
        # randomize the questions
        random.shuffle(questions)
        # initialize score accumulators
        player1_score = 0
        player2_score = 0
        # main game loop, 5 questions each for 10 rounds
        for turn in range(10):
            # find out whose turn it is and let them know
            player = turn % 2 + 1
            print(f"Player {player}...")
            time.sleep(1)
            # grab a question, shuffle its answers, and print out the info
            question = questions.pop()
            question.shuffle_answers()
            print(question.get_question())
            answers = question.get_answers()
            print("1:", answers[0])
            print("2:", answers[1])
            print("3:", answers[2])
            print("4:", answers[3])
            # get the user's answer
            answer = int(input()) - 1
            # check what they input and verify if it is correct or not
            if question.check_answer(answers[answer]):
                print("Correct")
                if player == 1:
                    player1_score += 1
                else:
                    player2_score += 1
            else:
                # if id didn't match above, it is incorrect
                print("Incorrect")
            # print out the extra trivia info
            print(question.get_extra_trivia())
            time.sleep(3)
        # check to see who won and let the players know
        if player1_score > player2_score:
            print(f"Player 1 wins {player1_score} - {player2_score}")
        elif player2_score > player1_score:
            print(f"Player 2 wins {player2_score} - {player1_score}")
        else:
            print("Tie game.")
    # function to load the questions from file and return the list
    def load_questions():
        # initialize empty lists
        questions = []
        answers = []
        # create the file reader generator
        line_gen = line_read()
        for line in line_gen:
            # questions start with a -, and extra trivia starts with @
            # the following line is the correct answer and then 3 incorrect answers
            if line.startswith("-"):
                # don't append the first time we see this
                if answers != []:
                    # create the question from the data read and append it to the list
                    questions.append(Question(question, answers.copy(), answers[0], extra_trivia))
                # start the process by setting the question and restart by clearing the answers list
                question = line.strip('-').strip()
                answers.clear()
            elif line.startswith("@"):
                # set the extra trivia info
                extra_trivia = line.strip("@").strip()
            else:
                # add the answer to the list
                answers.append(line.strip())
        return questions
    
    def line_read():
        # generator to open the questions file and yield each line
        with open('questions.txt', 'r') as file:
            for line in file:
                yield line
    main()
program_8()