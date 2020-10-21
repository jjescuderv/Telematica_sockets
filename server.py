import os
import json
import socket
import constants
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def handle_client(conn, addr):
    connected = True
    while connected:
        input_recv = conn.recv(constants.RCV_BUFFER_SIZE).decode(constants.FORMAT)
        recv = input_recv.split()
        command = recv[0]

        print(command)
        print(f'Received from { addr }')

        if command == constants.LIST_ALL:
            data = {}
            for r, d, f in os.walk(constants.PATH):
                if r != constants.PATH:
                    data[os.path.basename(r)] = f
            data_string = json.dumps(data)

            conn.send(bytes('[600] LIST RETRIEVED', constants.FORMAT))
            conn.send(bytes(data_string, constants.FORMAT))

        elif command == constants.CREATE_BUCKET:
            new_bucket = constants.PATH + f'/{ recv[1] }'
            try:
                os.mkdir(new_bucket)
            except OSError:
                conn.send(bytes('[406] BUCKET ALREADY EXISTS', constants.FORMAT))
            else:
                conn.send(bytes('[100] BUCKET CREATED', constants.FORMAT))

        elif command == constants.DELETE_BUCKET:
            new_bucket = constants.PATH + f'/{ recv[1] }'
            try:
                os.rmdir(new_bucket)
            except OSError:
                conn.send(bytes('[404] BUCKET NOT FOUND', constants.FORMAT))
            else:
                conn.send(bytes('[100] BUCKET DELETED', constants.FORMAT))

        elif command == constants.LIST_BUCKETS:
            pass
        elif command == constants.LIST_FILES:
            pass
        elif command == constants.UPLOAD_FILE:
            pass
        elif command == constants.DOWNLOAD_FILE:
            pass
        elif command == constants.DELETE_FILE:
            pass
        elif command == constants.DISCONNECT_COMMAND:
            print(f'[CLIENT DISCONNECTED] { addr } disconnected')
            conn.send(bytes('[300] DISCONNECTED', constants.FORMAT))
            connected = False
        else:
            conn.send(bytes('[400] UNKNOWN COMMAND', constants.FORMAT))

    conn.close()


def start():
    print('[STARTING] Server is starting... ')
    conn_tuple = (constants.SERVER_ADDRESS, constants.PORT)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(conn_tuple)
    server_socket.listen(constants.BACKLOG)
    print(f'[LISTENING] Server is listening to { constants.BACKLOG } users')

    while True:
        client_conn, client_addr = server_socket.accept()
        thread_client = threading.Thread( target=handle_client, args=(client_conn, client_addr) )
        thread_client.start()
        client_conn.send((f'[CONNECTED] Connected to the server from { client_addr }'.encode(constants.FORMAT)))
        print(f'[CLIENT CONNECTED] { client_addr } connected.')

# Not finished
def getErrorMessage(command, arguments):
    requirements = constants.COMMAND_REQUIREMENTS[command]
    if requirements[0] > arguments:
        return 401
    elif requirements[0] < arguments:
        return 402
    else:
        return 600
    

if __name__ == "__main__":
    start()