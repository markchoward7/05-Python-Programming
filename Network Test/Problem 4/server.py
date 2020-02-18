import socket

def main():
    # Create the socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set the socket options to prevent errono 98
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created.")
    # Bind the socket to accept any IP on port 9898
    port = 9898
    my_socket.bind(('', port))
    print(f"Socket bound to {port}.")
    # Tell the socket to listen
    my_socket.listen(1)
    print("Socket is listening...")
    # Call the run function
    run(my_socket)
    # Close the socket
    my_socket.close()

# Function to continously accept users, take their inputs, and send them the reversed string
def run(my_socket):
    # While loop to continously accept users
    while True:
        # Accept the connection
        user, user_address = my_socket.accept()
        # Print the connection information
        print('Connection established with:', user_address)
        # Receive the data from the user
        data = user.recv(512).decode()
        # Check for exit condition string
        if data == "TERMINATE SERVER":
            break
        # Reverse the string, encode it, and send it back to the user
        user.send(data[::-1].encode())

if __name__ == "__main__":
    main()