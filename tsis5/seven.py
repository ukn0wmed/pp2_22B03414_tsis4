import re

string = input("Enter a string in snake case: ")
pattern = r"_(\w)"

new_string = re.sub(pattern, lambda x: x.group(1).upper(), string)

print("New string in camel case: " + new_string)
