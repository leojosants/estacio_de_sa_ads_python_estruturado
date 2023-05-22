"""
    Implementar um solução em Python que resolva a seguinte questão:
        
        - Calcular o valor de uma compra, sendo que o preço unitário é R$10,00.
        
            - Se for feita uma compra de até 10 UN, não há descontos.
            - Para compras entre 11 UN e 20 UN é dado um desconto de 10%.
            - Acima de 20 UN, é dado um desconto de 20%
"""
print()

quantidade = eval(input('Informe a quantidade que deseja comprar: '))

PRECO_UNITARIO = 10.00
DESCONTO_10UN = 0.1
DESCONTO_20UN = 0.2

valorCompra = PRECO_UNITARIO * quantidade
valorFinal = 0.00

if(quantidade <= 10):
    valorFinal = valorCompra

elif(quantidade <= 20):
    valorFinal = valorCompra * (1 - DESCONTO_10UN)
else:
    valorFinal = valorCompra * (1 - DESCONTO_20UN)

print(f'\nValor da compra: R$ {valorCompra} | Valor final: R$ {valorFinal}')

print()
