import socket

def start_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define the server address (host, port)
    server_address = ('localhost', 12345)

    # Bind the socket to the server address
    server_socket.bind(server_address)

    print(f"Server is listening on {server_address[0]}:{server_address[1]}...")

    while True:
        # Wait for a message
        print("Waiting for a message...")
        data, client_address = server_socket.recvfrom(1024)

        try:
            print(f"Received: {data.decode()} from {client_address}")

            # Send a response back to the client
            message = "Received your message!"
            server_socket.sendto(message.encode(), client_address)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    start_server()