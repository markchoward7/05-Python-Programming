import socket

def main():
    # Create the socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server on port 9898
    my_socket.connect(('localhost', 9898))
    # Get the data from the user to send to the server
    data = input("Enter a string to alter\n")
    # Encode and send the data
    my_socket.send(data.encode())
    # Receive, decode, and print the output from the server
    print(my_socket.recv(512).decode())
    # Close the socket
    my_socket.close()

if __name__ == "__main__":
    main()