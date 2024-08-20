import socket
import threading
import sys

def receive_messages(client_socket):
    """Receives messages from the server and prints them."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            print("Connection lost.")
            client_socket.close()
            break

def send_messages(client_socket):
    """Sends messages to the server."""
    while True:
        message = input()
        if message:
            client_socket.send(message.encode('utf-8'))

def start_client():
    """Starts the chat client."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))  # Connect to the server
    print("Connected to the server. Type your messages below:")

    # Start threads for receiving and sending messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    receive_thread.start()
    send_thread.start()

if __name__ == "__main__":
    start_client()
