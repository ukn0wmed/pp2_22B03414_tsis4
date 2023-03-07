import os

path = "/path/to/directory"

if os.path.exists(path):
    if os.access(path, os.R_OK):
        print("Readable")
    if os.access(path, os.W_OK):
        print("Writable")
    if os.access(path, os.X_OK):
        print("Executable")
else:
    print("Path does not exist")
