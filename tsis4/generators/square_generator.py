def squares_generator(N):
    for i in range(1, N+1):
        yield i*i

squares = squares_generator(5)

for square in squares:
    print(square)