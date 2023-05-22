
# Implementar uma solução em Python que retorne o menor elemento de uma lista

def encontrarMenorElemento(lista):
    menor = lista[0]

    for elemento in lista:
        if elemento < menor:
            menor = elemento

    return menor

lista = [2, 10, 3, 1, 4, 5]
menorElemento = encontrarMenorElemento(lista)

print(f'\nO menor elemento encontrado na lista foi: {menorElemento} \n')
