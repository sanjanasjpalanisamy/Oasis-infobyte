import socket
import threading

# List to keep track of connected clients
clients = []

def broadcast(message, client_socket):
    """Broadcasts a message to all clients except the sender."""
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client_socket):
    """Handles a single client connection."""
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, client_socket)
            else:
                # Remove client from list if connection is closed
                client_socket.close()
                clients.remove(client_socket)
                break
        except:
            client_socket.close()
            clients.remove(client_socket)
            break

def start_server():
    """Starts the chat server."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5555))  # Bind to all interfaces on port 5555
    server_socket.listen(5)
    print("Server started. Listening for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"New connection from {addr}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
