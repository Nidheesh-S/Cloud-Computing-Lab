import socket
import threading

clients = []

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                remove(client)

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                reversed_message = message[::-1]
                broadcast(reversed_message, client_socket)
            else:
                remove(client_socket)
        except:
            continue

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print(f"Server is listening on {server_address[0]}:{server_address[1]}...")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    start_server()