def divisible_by_3_and_4_generator(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


ranger = int(input("Please, enter the number: "))
for number in divisible_by_3_and_4_generator(ranger):
    print(number, end=' ')
