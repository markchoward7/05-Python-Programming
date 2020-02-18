import base64

def challenge1():
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    to_decipher = 'MYXQBKDEVKDSYXC'

    shift = 0
    while True:
        result = ''
        shift += 1
        for char in to_decipher:
            result += alpha[(alpha.find(char) + shift) % 26]
        print(result)
        response = input("Finished? y/n\n")
        if response == 'y':
            break

def challenge2():
    to_decipher = 'VGhpcyBpcyB0b28gZWFzeQ=='
    print(base64.b64decode(to_decipher).decode('utf-8'))

def challenge2_1():
    to_decipher = b'VWtkc2EwbEliSFprVTBJeFl6SlZaMWxUUW5OaU1qbDNVSGM5UFE9PQ=='
    while True:
        # try:
        to_decipher = base64.b64decode(to_decipher)
        # except:
        #     to_decipher += b'='
        print(to_decipher)
        response = input("Finished? y/n\n")
        if response == 'y':
            break

def challenge3():
    to_decipher = 'kquht}'
    key = 0
    while True:
        result = ''
        key += 1
        for char in to_decipher:
            result += chr(ord(char) ^ key)
        print(result)
        response = input("Finished? y/n\n")
        if response == 'y':
            break

# def challenge3_1():
#     to_decipher = bytearray.fromhex('70155d5c45415d5011585446424c').decode('utf-8')
#     chars = [chr(i) for i in range(127)]
#     key = [chars[0], chars[0]]

#     while True:
#         result = ''
#         try:
#             key[1] = chars[chars.index(key[1]) + 1]
#         except:
#             try:
#                 key[0] = chars[chars.index(key[0]) + 1]
#             except:
#                 break
#             key[1] = chars[0]
#         for char in to_decipher:
#             result += chr(ord(char) ^ ord(key[0]))
#             result += chr(ord(char) ^ ord(key[1]))
#         print(result)
# challenge3_1()

# def challenge3_1():
#     to_decipher = bytearray.fromhex('70155d5c45415d5011585446424c').decode('utf-8')
#     chars = [str(i) for i in range(10)]
#     key = ['0', '0']

#     while True:
#         result = ''
#         try:
#             key[1] = chars[chars.index(key[1]) + 1]
#         except:
#             try:
#                 key[0] = chars[chars.index(key[0]) + 1]
#             except:
#                 break
#             key[1] = chars[0]
#         for char in to_decipher:
#             result += chr(ord(char) ^ ord(key[0]))
#             result += chr(ord(char) ^ ord(key[1]))
#         print(result)
# challenge3_1()

# def challenge3_1():
#     to_decipher = bytearray.fromhex('70155d5c45415d5011585446424c').decode('utf-8')
#     key = 0

#     while key < 100:
#         key += 1
#         result = ''
#         for char in to_decipher:
#             result += chr(ord(char) ^ key)
#         print(result)
# challenge3_1()