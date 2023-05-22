""" 
    print()

    while True:
        palavra = input('Entre com uma palavra, para sair digite [SAIR]: ')

        if palavra == 'sair':
            break

    print('Você digitou sair e agora está fora \n')
"""

# Caso haja vários laços aninhados, o break será relativo ao laço em que estiver inserido.
print()

while True:
    print('Você está no primeiro laço.')

    opcao1 = input('Deseja sair dele? Digite SIM para isso. ')

    if opcao1 == 'SIM':
        break  # este break é do primeiro laço

    else:
        while True:
            print('Você está no segundo laço.')

            opcao2 = input('Deseja sair dele? Digite SIM para isso. ')

            if opcao2 == 'SIM':
                break  # este break é do segundo laço

        print('Você saiu do segundo laço.')

print('Você saiu do primeiro laço \n')
