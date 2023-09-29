import tkinter as tk
import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            chat_box.insert(tk.END, message + '\n')
        except:
            break

def send_message(event=None):
    message = my_message.get()
    my_message.set("")
    client_socket.send(message.encode('utf-8'))

def on_closing():
    client_socket.close()
    root.quit()

root = tk.Tk()
root.title("Chat Application")

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_box = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
chat_box.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=chat_box.yview)

my_message = tk.StringVar()
entry_field = tk.Entry(root, textvariable=my_message)
entry_field.bind("<Return>", send_message)
entry_field.pack(pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()