import random
import time
import pickle
import os

# many global variables
puzzle = ''
user = ''
users = {}
guessed_letters = []
incorrect_guesses = 0
# this one is just for the forever alone mod
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def main():
    # grab the appropriate global variables
    global user, puzzle, users
    # intro and set up the user on the first time running
    if user == '':
        print("Welcome to hangman")
        print("Guess letters to fill in the blanks")
        print("6 incorrect guesses and you lose")
        # load the userlist from file
        users = load_users()
        # get the username from user input, they will either choose one already made or make a new one
        print("Are you a returning user? (y/n)")
        if input().lower() == 'y':
            while user == '':
                print("Enter your username")
                user = input()
                if user not in users:
                    print("%s not found, would you like to try another username? (y/n)" % user)
                    if input().lower() == 'y':
                        user = ''
                    else:
                        create_user()
        else:
            create_user()
    # call the random puzzle method
    puzzle = choose_puzzle()
    # ask if they want to use the forever alone mod and then call display with true if so, otherwise just call display
    print("Would you like to watch the computer play instead of playing this yourself for some weird reason? (y/n)")
    if input().lower() == 'y':
        display(True)
    else:
        display()    
    

def load_users():
    # function to load the users with pickle from the users.dat file
    # returns a dictionary, is empty if no file found
    file_path = "users.dat"
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    else:
        return {}


def save_data():
    # saves the users dictionary with pickle
    with open("users.dat", 'wb') as file:
        pickle.dump(users, file)

def create_user():
    # grab the appropriate global variables
    global user, users
    # get the username from input
    print("Enter a username")
    username = ''
    # make sure the username isn't already taken
    # if we have good input, add the user to the dictionary and set them to 0 wins
    while username == '':
        username = input()
        if username in users:
            print("Username already taken. Please try another.")
            username = ''
        else:
            user = username
            users[user] = 0

def leaderboard():
    # print the top 5 players in the leaderboard
    print("Leaderboard:")
     # put the users into a list of tuples with names and scores reversed
    sorted_users = sorted([(score, name) for name, score in users.items()], reverse = True)
    # print out the top 5 from our list
    for index, user in enumerate(sorted_users):
        if index >= 5:
            break
        else:
            print(f"\t{user[1]}\t{user[0]}")
    print("Thanks for playing!")

def choose_puzzle():
    # open the file of puzzles and pick one at random and return it
    with open('word_bank.txt', 'r') as file:
        puzzles = list(file)
    return random.choice(puzzles).strip().upper()

def display(alone=False):
    # display function, alone optional parameter used to turn on forever alone mod
    puzzle_display = ''
    global users
    # loop through each character in the puzzle, place guessed letters in the right spot
    # otherwise put hyphens, and spaces as needed
    # all remaining characters are underscores
    for char in puzzle:
        if char == ' ':
            puzzle_display += '  '
        elif char == '-':
            puzzle_display += '-'
        elif char in guessed_letters:
            puzzle_display += char
        else:
            puzzle_display += '_'
        puzzle_display += ' '
    print(puzzle_display)
    # check if there are any underscores to see if the player won
    if '_' not in puzzle_display:
        # if not on forever alone, increment score and save data
        if not alone:
            users[user] += 1
            save_data()
        # print a win message and allow them to play again
        print("You win")
        print("Play again? (y/n)")
        if input().lower() == 'y':
            # if they play again, call the reset to clean up and then go back to main
            reset()
            main()
        else:
            # if they don't play again, display the leaderboard
            leaderboard()
    # check if they have too many incorrect guesses
    elif incorrect_guesses >= 6:
        # notify them they lost, print the answer, ask if they want to play again
        print("You lose")
        print(puzzle)
        print("Play again? (y/n)")
        if input().lower() == 'y':
            # if they play again, call the reset to clean up and then go back to main
            reset()
            main()
        else:
            # if they don't play again, display the leaderboard
            leaderboard()
    else:
        # if there was no end state condition, call either forever alone or user choice
        if alone:
            forever_alone()
        else:
            user_choice()

def reset():
    # function resets the guessed letters, letters, and incorrect guesses variables
    # called between games
    global guessed_letters, letters, incorrect_guesses
    if len(letters) < 26:
        letters += guessed_letters
    guessed_letters = []
    incorrect_guesses = 0

def user_choice():
    # function to take the player's guesses
    # starts by printing what they have already guessed and how many incorrect guesses they have
    print("Here are the letters you've already guessed", sorted(guessed_letters))
    global incorrect_guesses
    print("Incorrect guess count:", incorrect_guesses)
    guess = ''
    # while loop fo rinput validation
    while guess == '':
        print("Enter a guess.")
        guess = input().upper()
        # make sure the guess is a letter and not more than 1 letter
        if not guess.isalpha() or len(guess) != 1:
            print("Your guess must be a single letter")
            guess = ''
        # make sure the guess wasn't already guessed
        elif guess in guessed_letters:
            print("You've already guessed that letter, try again.")
            guess = ''
        else:
            # if the guess was valid, append it to the guessed letters, then check if it is correct
            guessed_letters.append(guess)
            if guess in puzzle:
                print("Correct guess")
            else:
                print("Incorrect guess")
                incorrect_guesses += 1
    # afterwards call the display again
    time.sleep(1)
    display()

def forever_alone():
    # function for the forever alone mod of the game
    # takes a random letter from the letters list and guesses it
    # it is terrible at winning
    global incorrect_guesses
    print("Incorrect guess count:", incorrect_guesses)
    time.sleep(1)
    # pop the letter chosen so it won't be chosen again
    choice = letters.pop(random.randint(0,len(letters)-1))
    print("The computer guesses %s" % choice)
    time.sleep(1)
    if choice in puzzle:
        print("Correct guess")
    else:
        print("Incorrect guess")
        incorrect_guesses += 1
    # append to guessed letters still since we use this to fill the display function
    guessed_letters.append(choice)
    display(True)

main()