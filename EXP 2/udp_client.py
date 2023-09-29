import socket

def start_client():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define the server address (host, port)
    server_address = ('localhost', 12345)

    try:
        # Send data to the server
        message = "Hello, server!"
        client_socket.sendto(message.encode(), server_address)

        # Receive and print the response from the server
        data, server_address = client_socket.recvfrom(1024)
        print(f"Received: {data.decode()} from {server_address}")

    finally:
        # Clean up the connection
        client_socket.close()

if __name__ == '__main__':
    start_client()