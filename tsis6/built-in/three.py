def is_palindrome(string):
    return string == string[::-1]


string = "racecar"
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a palindrome")
