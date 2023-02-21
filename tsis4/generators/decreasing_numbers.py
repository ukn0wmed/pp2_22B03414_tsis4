def all_numbers(n):
    while n >= 0:
        yield n
        n -= 1


for i in all_numbers(15):
    print(i)