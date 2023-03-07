import time
from math import sqrt


def square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return sqrt(number)


number = 25100
milliseconds = 2123
result = square_root(number, milliseconds)
print(
    f"Square root of {number} after {milliseconds} milliseconds is {result}")
