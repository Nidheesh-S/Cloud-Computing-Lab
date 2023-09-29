import tkinter as tk
import threading
import socket

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            message = message[::-1]  # Reverse the message
            chat_box.insert(tk.END, message + '\n')
        except:
            # An error will occur if the connection is lost
            print("An error occurred!")
            break

# Function to send messages to the server
def send_message(event=None):
    message = my_message.get()
    my_message.set("")  # Clear the input field
    client_socket.send(message.encode('utf-8'))

# Create the main window
root = tk.Tk()
root.title("Chat Application")

# Create a frame for the chat history
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a scrollbar for the chat history
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text widget for displaying the chat history
chat_box = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
chat_box.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=chat_box.yview)

# Create an entry field for sending messages
my_message = tk.StringVar()
entry_field = tk.Entry(root, textvariable=my_message)
entry_field.bind("<Return>", send_message)
entry_field.pack(pady=10)

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Set up the connection to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 56789))

# Start a separate thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

# Start the GUI main loop
root.mainloop()

# Close the socket when the GUI is closed
client_socket.close()