import socket
import constants

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    print('[CONNECTING] Connecting to server... ')
    server_tuple = (constants.SERVER_ADDRESS, constants.PORT)
    client_socket.connect(server_tuple)
    local_tuple = client_socket.getsockname()
    print(f'[CONNECTED] Connected from { local_tuple }')

    command = input()
    #command = command_input.split()
    while command != constants.DISCONNECT_COMMAND:
        if command == constants.SEND_COMMAND:
            data = input('Enter data: ')
        else:
            data = 'Bad command'
            
        client_socket.send(bytes((command + ' ' + data), constants.FORMAT))
        command = input()

    client_socket.send(bytes((command), constants.FORMAT))
    client_socket.close()

if __name__ == "__main__":
    main()