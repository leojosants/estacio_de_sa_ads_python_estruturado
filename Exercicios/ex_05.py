def fatorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5)
        # return n * fatorial(n - 1)

print(fatorial(5))

""" Para que a função seja recursiva, na linha 6 deve-se invocar a função fatorial() """