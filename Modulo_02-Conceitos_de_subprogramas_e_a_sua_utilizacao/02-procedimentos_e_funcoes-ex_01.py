
# Implementar uma solução em Python que retorne a soma de todos os lementos pares da lista

def ehPar(n):
    resultado = (n % 2 == 0)
    return resultado

def retornarSomaDePares(lista):
    soma = 0

    for numero in lista:
        if ehPar(numero):
            soma += numero

    return soma

lista = [10, 2, 5, 7, 6, 3]
somaPares = retornarSomaDePares(lista)
print(f'\nA soma de todos os elementos pares da lista é: {somaPares}')
