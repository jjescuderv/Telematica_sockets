import os
import socket

FORMAT = 'utf-8'
SERVER_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT = 9090
BACKLOG = 10
RCV_BUFFER_SIZE = 1024
PATH = 'C:/Users/Juan Escudero/Desktop/Telematica PR1/server_files'

CHANGE_DIRECTORY = 'CD'
LIST_ALL = 'ALL'                # Lists everything                         |    No parameters
CREATE_BUCKET = 'BUCKETC'       # Create a new bucket                      |    bucket name
DELETE_BUCKET = 'BUCKETD'       # Delete a selected bucket                 |    bucket id
LIST_BUCKETS = 'BUCKETL'        # List all buckets                         |    No parameters
LIST_FILES = 'FILEL'            # List all files of an existing bucket     |    bucket id
UPLOAD_FILE = 'UPFILE'          # Upload a file to the server              |    file name and extension
DOWNLOAD_FILE = 'DWFILE'        # Download a file from the server          |    bucket id, file id
DELETE_FILE = 'DEFILE'          # Delete a file from an existing bucket    |    bucket id, file id
COMMAND_INFO = 'HELP'
DISCONNECT_COMMAND = 'QUIT'     # Disconnects from server                  |    No parameters

COMMAND_MESSAGE = {
    100: '[100] BUCKET CREATED',
    101: '[101] FILE CREATED',
    200: '[200] BUCKET DELETED',
    201: '[201] FILE DELETED',
    300: '[300] DISCONNECTED',
    400: '[400] UNKNOWN COMMAND',
    401: '[401] TOO MANY ARGUMENTS',
    402: '[402] NOT ENOUGH ARGUMENTS',
    403: '[403] INVALID ARGUMENTS',
    404: '[404] BUCKET NOT FOUND',
    405: '[405] FILE NOT FOUND',
    406: '[406] FILE ALREADY EXISTS',
    407: '[407] BUCKET ALREADY EXISTS',
    500: '[500] FILE UPLOADED',
    501: '[501] FILE DOWNLOADED',
    600: '[600] LIST RETRIEVED',
}
# Not used yet
COMMAND_REQUIREMENTS = {  
    # 'COMMAND': [ARGUMENTS+1, TYPE OF ARGUMENT]      
    'ALL': [1, 'Text'],
    'BUCKETC': [2, 'Text'],
    'BUCKETD': [2, 'Number'],
    'BUCKETL': [1, 'Text'],
    'FILEL': [2, 'Number'],
    'UPFILE': [2, 'Text'],
    'DWFILE': [3, 'Number'],
    'DEFILE': [3, 'Number'],
    'QUIT': [1, 'Text']
}
