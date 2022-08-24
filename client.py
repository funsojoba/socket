import socket


def client():
    client_socket = socket.socket()
    host = socket.gethostname()
    port = 5000
    client_socket.connect((host, port))
    
    name = input("Enter your name: ")
    client_socket.send(name.encode())
    
    print(client_socket.recv(1024).decode())
    
    
    
if __name__ == '__main__':
    client()