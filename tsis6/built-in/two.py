def count_case(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count


string = "Hello, World!"
upper, lower = count_case(string)
print("Uppercase letters:", upper)  # Output: 2
print("Lowercase letters:", lower)  # Output: 8
