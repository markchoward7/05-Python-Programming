import random

scripts = ['The [adj0] [noun0] [verb0] to the [adj1] [noun1]. Then a [noun2] [adv0] [verb1].',
            'A [adj0], [adj1] [noun0] [verb0] a [adj2] [noun1]. While this was happening, a [adj3] [noun2] [adv0], [adv1] [verb1].']

def start_game():
    scriptNum = random.randint(0, len(scripts)-1)
    script = scripts[scriptNum]
    adjectiveCount = script.count("[adj")
    nounCount = script.count("[noun")
    adverbCount = script.count("[adv")
    verbCount = script.count("[verb")
    for i in range(adjectiveCount):
        while True:
            print("Enter an adjective")
            command = input()
            if command.isalpha():
                print(f"{command} accepted")
                script = script.replace(f"[adj{i}]",command)
                break
            else:
                print("You can't use numbers or special characters")
    for i in range(nounCount):
        while True:
            print("Enter a noun")
            command = input()
            if command.isalpha():
                print(f"{command} accepted")
                script = script.replace(f"[noun{i}]",command)
                break
            else:
                print("You can't use numbers or special characters")
    for i in range(adverbCount):
        while True:
            print("Enter an adverb")
            command = input()
            if command.isalpha():
                print(f"{command} accepted")
                script = script.replace(f"[adv{i}]",command)
                break
            else:
                print("You can't use numbers or special characters")
    for i in range(verbCount):
        while True:
            print("Enter a verb")
            command = input()
            if command.isalpha():
                print(f"{command} accepted")
                script = script.replace(f"[verb{i}]",command)
                break
            else:
                print("You can't use numbers or special characters")
    print(script)
    print("Would you like to play another game? (yes/no)")
    command = input().lower()
    if command == "yes":
        start_game()
    

print('Mad Libs')
print("Would you like to play a game? (yes/no)")
command = input().lower()
if command == "yes":
    start_game()