import os

path = "delete.txt"

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("No write access")
else:
    print("Path does not exist")
