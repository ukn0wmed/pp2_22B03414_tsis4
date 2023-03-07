my_list = ["apple", "banana", "cherry"]
filepath = "writein.txt"

with open(filepath, "w") as file:
    for item in my_list:
        file.write(f"{item}\n")
