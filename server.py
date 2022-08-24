import socket


def main():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = data.upper()
        conn.send(bytes(f"Welcome to the server {data}", "utf-8"))
        conn.close()
    

if __name__ == '__main__':
    main()