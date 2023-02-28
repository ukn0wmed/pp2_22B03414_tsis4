import re

string = input("Enter a string: ")
pattern = r"a.*b$"

if re.search(pattern, string):
    print("Match found!")
else:
    print("Match not found!")
