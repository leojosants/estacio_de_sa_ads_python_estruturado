"""
    Implementar um solução em Python que faça o tratamento de exceção de divisão por xero
"""
print()

def dividir(x, y):
    try:
        resultado = x / y
        print(f'O resultado de {x} / {y} é: {resultado}')
    except ZeroDivisionError:
        print('Não é possivel realizar divisão por zero!')


dividir(3, 0)
dividir(3, 3)
print()
