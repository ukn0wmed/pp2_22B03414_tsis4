import string
import os

directory = "alph"
if not os.path.exists(directory):
    os.makedirs(directory)

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as file:
        file.write(f"This is {filename}")
