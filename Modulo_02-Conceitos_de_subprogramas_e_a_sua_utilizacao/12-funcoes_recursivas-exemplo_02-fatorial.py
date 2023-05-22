# Implementação na forma RECURSIVA
def fatorialRecursivo(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fatorialRecursivo(n - 1)


# Implementação na forma CLÀSSICA
def fatorialClassico(n):
    fat = 1

    if (n == 0 or n == 1):
        return fat

    else:
        for x in range(2, n + 1):
            fat = fat * x

        return fat


numero = 5
print(f'{fatorialClassico(numero)}')
print(f'{fatorialRecursivo(numero)}')
