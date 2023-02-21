print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))  # Those are returning FALSE, everything else mostly true (it's about variables)
print(bool(17 == 18))

a = 574
b = 574
print(bool((a-b) == 0))
c = a * b
print(bool(c == (a * b)))
