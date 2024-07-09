import socket

def main():
    print("Waiting for connection")
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        connection, address = server_socket.accept()
        print(f"Connected from {address}")

        data = connection.recv(1024)
        result = data.decode().split("\r\n")

        res_200 = b"HTTP/1.1 200 OK\r\n\r\n"
        res_400 = b"HTTP/1.1 404 Not Found\r\n\r\n"
        res = result[0].split(" ")
        
        if res[1] == "/":
            connection.sendall(res_200)
        elif res[1].split("/")[1] == "echo":
            try:
                content = res[1].split("/")[2]
                connection.sendall(
                    f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(content)}\r\n\r\n{content}".encode()
                )
            except:
                connection.sendall(res_400)
        elif res[1].split("/")[1] == "user-agent":
            try:
                content = [x for x in result if "User-Agent" in x][0].split(": ")[1]
                connection.sendall(
                    f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(content)}\r\n\r\n{content}".encode()
                )
            except:
                 connection.sendall(res_400)
        else:
            connection.sendall(res_400)
        connection.close()

if __name__ == "__main__":
    main()
