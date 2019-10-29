# Location of the encoded lyrics
filePath = r"03_Flow_Control\performance_labs\lab3B\file.txt"

# With statement to open the file as file
with open(filePath, "r") as file:
    # Read the file
    text = file.readline()
    # Initialize a string accumulator
    newText = ""
    # For each character, get the ordinal, XOR 27 it, then convert back to a character and add to accumulator
    for char in text:
        newText += (chr(ord(char)^27))
    # Print result
    print(newText)