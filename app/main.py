import socket


def main():
    print("Waiting for connection")
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    
    # server_socket.accept() returns a Tuple so we store them in two variables, connection & address
    connection, address = server_socket.accept()
    # print( addr[0])
    # server_socket.accept()[0].sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    
    while True:
        data = connection.recv(1024)
        # print("Print decoded data.")

        result = data.decode().split("\r\n")
        
        res_200 = b"HTTP/1.1 200 OK\r\n\r\n"
        res_400 = b"HTTP/1.1 404 Not Found\r\n\r\n"
        if result[0].split(" ")[1] == "/":
            connection.sendall(res_200)
        else:
            connection.sendall(res_200)
        
        connection.close()



if __name__ == "__main__":
    main()
