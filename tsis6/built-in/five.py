def all_true(tuple):
    return all(tuple)


tuple1 = (True, True, False, True)
tuple2 = (True, True, True, True)
print(all_true(tuple1))
print(all_true(tuple2))
