import re

string = input("Enter a string: ")
pattern = r"ab{2,3}"

if re.search(pattern, string):
    print("Match found!")
else:
    print("Match not found!")
