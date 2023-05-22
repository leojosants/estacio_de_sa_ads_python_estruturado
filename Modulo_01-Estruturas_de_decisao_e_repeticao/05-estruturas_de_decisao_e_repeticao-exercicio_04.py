"""
    Implementar uma solução em Python que some todos os numeros pares de uma lista    
"""
print()

somaPares = 0

lista = [10, 2, 5, 7, 6, 3]

n = len(lista)

for i in range(n):
    if lista[i] % 2 == 0:
        somaPares += lista[i]

print(f'A soma de todos os número pares da lista é: {somaPares}')
print()
