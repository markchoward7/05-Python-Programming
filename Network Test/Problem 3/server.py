import socket

def main():
    # Create the socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set the socket options to prevent errono 98
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to accept any IP on port 9898
    my_socket.bind(('', 9898))
    # Tell the socket to listen
    my_socket.listen(1)
    # Accept the connection
    user = my_socket.accept()[0]
    # Encode and send the output of the replace function back to the user
    user.send(replace(user).encode())
    # Close the socket
    my_socket.close()

# Function to get the data from the user and return with the vowels replaced with #
def replace(user):
    # List of vowels to replace, including all instances of y
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    # Get the data from the user client
    data = user.recv(512).decode()
    # Accumulator string
    output = ''
    # Loop through the string, check if it is a vowel, if so add a #, otherwise add the char
    for char in data:
        if char.lower() in vowels:
            output += '#'
        else:
            output += char
    # Return the results of the loop
    return output

if __name__ == "__main__":
    main()