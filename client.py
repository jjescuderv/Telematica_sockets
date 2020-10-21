import socket
import constants

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    print('[CONNECTING] Connecting to server... ')
    server_tuple = (constants.SERVER_ADDRESS, constants.PORT)
    client_socket.connect(server_tuple)
    print(client_socket.recv(constants.RCV_BUFFER_SIZE).decode(constants.FORMAT))
    command = ''

    while command != constants.DISCONNECT_COMMAND:
        client_input = input()
        client_arr = client_input.split()
        command = client_arr[0]
        if command == '':
            print("Invalid input")
        else:
            client_socket.send(bytes(client_input, constants.FORMAT))

        print(client_socket.recv(constants.RCV_BUFFER_SIZE).decode(constants.FORMAT))
        if command == constants.LIST_ALL or command == constants.LIST_BUCKETS or command == constants.LIST_FILES:
            print(client_socket.recv(constants.RCV_BUFFER_SIZE).decode(constants.FORMAT))

    client_socket.close()

if __name__ == "__main__":
    main()