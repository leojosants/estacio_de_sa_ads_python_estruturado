def foo(n):
    if (n > 1):
        return n * foo(n - 1)
    print(n)
    return n


print(foo(4))
