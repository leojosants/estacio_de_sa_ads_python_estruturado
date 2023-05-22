
# Implementar uma solução em Python que determine se um número é ou não Primo

def ehPrimo(n):
    if (n < 2):
        return False

    i = n // 2

    while (i > 1):
        if (n % i == 0):
            return False

        i -= 1

    return True

#

def imprimirResultado(numero, resultado):
    msg = f'O número {numero} Não é Primo!'

    if(resultado):
        msg = f'O número {numero} é Primo!'
    
    return msg

#

numero = 7
resultado = ehPrimo(numero)
msg = imprimirResultado(numero, resultado)
print(f'\n{msg}')
