import os

path = "/path/to/file.txt"

if os.path.exists(path):
    print("Path exists")
    directory, filename = os.path.split(path)
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
else:
    print("Path does not exist")
