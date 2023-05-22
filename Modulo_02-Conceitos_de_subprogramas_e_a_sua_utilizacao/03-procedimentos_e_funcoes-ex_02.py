
# Implementar uma solução em Python que calcule o fatorial de um número

def fatorialInterativo(n):
    f = 1

    for i in range(1, n + 1):
        f *= i

    return f


def fatorialRecursivo(n):
    if ((n == 0) or (n == 1)):
        return 1

    return n * fatorialRecursivo(n - 1)


numero = 5
print(f'\nResultado do fatorial de {numero} com a função interativa: {fatorialInterativo(numero)}')
print(f'Resultado do fatorial de {numero} com a função recursiva: {fatorialRecursivo(numero)} \n')
