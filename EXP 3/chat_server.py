import socket
import threading

# List to keep track of connected clients
clients = []

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove broken connections
                remove(client)

# Function to remove a client from the list
def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                reversed_message = message[::-1]  # Reverse the message
                broadcast(reversed_message, client_socket)
            else:
                remove(client_socket)
        except:
            continue

# Start the server
def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address (host, port)
    server_address = ('localhost', 56789)

    # Bind the socket to the server address
    server_socket.bind(server_address)

    # Start listening for incoming connections
    server_socket.listen(5)

    print(f"Server is listening on {server_address[0]}:{server_address[1]}...")

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)

        # Start a separate thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    start_server()