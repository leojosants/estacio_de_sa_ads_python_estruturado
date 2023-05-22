"""
    Implementar um solução em Python que faça o tratamento de exceção para verificar se uma entrada é numérica e que além disso, insista que o usuário digite um numero válido 
"""

while True:
    try:
        numero = int(input('\nEntre com um número: '))
        break
    except ValueError:
        print('--> Número não válido, tente novamente!')
