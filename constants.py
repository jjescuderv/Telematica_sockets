#import socket
# SERVER_ADDRESS = socket.gethostbyname(socket.gethostname())

FORMAT = 'utf-8'
SERVER_ADDRESS = '127.0.0.1'
PORT = 9090
BACKLOG = 10
RCV_BUFFER_SIZE = 1024


# COMMANDS
CREATE_BUCKET = 'BUCKETC'   # Create a new bucket                      |    bucket name
DELETE_BUCKET = 'BUCKETD'   # Delete a selected bucket                 |    bucket id
LIST_BUCKETS = 'BUCKETL'    # List all buckets                         |    No parameters
LIST_FILES = 'FILEL'        # List all files of an existing bucket     |    bucket id
UPLOAD_FILE = 'UPFILE'      # Upload a file to the server              |    file name and extension
DOWNLOAD_FILE = 'DWFILE'    # Download a file from the server          |    bucket id, file id
DELETE_FILE = 'DEFILE'      # Delete a file from an existing bucket    |    bucket id, file id


# TEMP
DISCONNECT_COMMAND = 'QUIT'
SEND_COMMAND = 'SEND'

# -------------------- BUCKETS COMMANDS --------------------
# BUCKETL
# BUCKETC
# BUCKETU {ID} -> INPUT FILE
# BUCKETD {ID}

# ---------------------- FILE COMMANDS ----------------------
# FILEUP {PATH}
# FILEDW {PATH}
# FILEDE {BUCKET ID} {FILE ID}
