import socket

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address (host, port)
    server_address = ('localhost', 12345)

    try:
        # Connect the socket to the server's address
        client_socket.connect(server_address)

        # Send data to the server
        message = "Hello, server!"
        client_socket.sendall(message.encode())

        # Receive and print the response from the server
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")

    finally:
        # Clean up the connection
        client_socket.close()

if __name__ == '__main__':
    start_client()





