from functools import reduce


def multiply(numbers):
    return reduce(lambda x, y: x * y, numbers)


numbers = [2, 3, 4, 5]
result = multiply(numbers)
print(result)
