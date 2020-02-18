text = input("Give me a string!\n")
key = input("Give me a key?\n")

for index, char in enumerate(text):
    print(chr(ord(key[index % len(key)]) ^ ord(char)))