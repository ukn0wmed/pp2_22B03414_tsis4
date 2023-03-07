import os

path = "C:/Users/ukn0w/PycharmProjects/pythonProject/tsis6" # можно поставить точку

# List only directories
print("Directories:")
for dir in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir)):
        print(dir)

# List only files
print("Files:")
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)

# List all directories and files
print("All directories and files:")
for item in os.listdir(path):
    print(item)
