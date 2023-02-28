import re

string = input("Enter a string: ")
pattern = r"([A-Z][a-z]+)"

new_string = re.sub(pattern, r" \1", string)

print("New string: " + new_string)
