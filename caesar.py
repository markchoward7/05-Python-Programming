alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

text = input("Give me a string!\n").upper()
shift = int(input("Give me a value to shift by!\n"))

result = ''

for char in text:
    result += alpha[(alpha.find(char) + shift) % 26]

print(result)