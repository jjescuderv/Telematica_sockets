import socket
import constants
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def handle_client(conn, addr):
    connected = True
    while connected:
        data_recv = conn.recv(constants.RCV_BUFFER_SIZE).decode(constants.FORMAT)

        if data_recv:
            data = data_recv.split()
            print(data[0])

            if data[0] == constants.SEND_COMMAND:
                print(f'{ data[1] } from { addr }')
            elif data[0] == constants.DISCONNECT_COMMAND:
                print(f'[CLIENT DISCONNECTED] { addr } disconnected')
                connected = False

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
        print(f'[CLIENT CONNECTED] { client_addr } connected.')


if __name__ == "__main__":
    start()