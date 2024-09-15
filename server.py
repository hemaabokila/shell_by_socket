from socket import socket,AF_INET,SOCK_STREAM
def server():
    end="<end>"
    s_socket=socket(AF_INET,SOCK_STREAM)
    sr_ip="192.168.1.14"
    sr_port=2001
    sock_connect=(sr_ip,sr_port)
    s_socket.bind(sock_connect)
    s_socket.listen(1)
    print("waiting.....")
    s_socket,c_address=s_socket.accept()
    print("connect from",c_address[0],":",c_address[1])
    try:
        while True:
            command = input(">> ")
            s_socket.send(command.encode())
            if command.lower() == "exit":
                s_socket.close()
                break
            elif command == "":
                continue 
            else:
                full_result= b""
                while True:
                    result = s_socket.recv(1024)
                    if result.endswith(end.encode()):
                        result = result[:-len(end)]
                        full_result += result
                        print(full_result.decode())
                        break
    except Exception as e:
        print(e)
        s_socket.close()
server()
