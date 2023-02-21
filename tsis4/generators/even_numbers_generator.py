def even_numbers_generator(n):
    for i in range(0, n+1, 2):
        yield i


n = int(input("Enter a number: "))


even_numbers = even_numbers_generator(n)

print("Even numbers between 0 and", n, "are: ")
for number in even_numbers:
    if number == n or number == n - 1:
        print(number, end='')
    else:
        print(number, end=', ')
