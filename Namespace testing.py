def foo(x, y):
    a = 42
    x, y = y, x
    print(a, b, x, y)


a, b, x, y = 1, 2, 3, 4
foo(17, 4)
print(a, b, x, y)
