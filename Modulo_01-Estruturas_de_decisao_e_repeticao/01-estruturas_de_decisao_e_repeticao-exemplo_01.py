# Implementar um solução em Python que receba dois números e identifique qual o maior deles.
print()

primeiroNumero = eval(input('Informe o primeiro número: '))
segundoNumero = eval(input('Informe o segundo número: '))

maiorNumero = primeiroNumero

if(segundoNumero > maiorNumero):
    maiorNumero = segundoNumero
    
print(f'O maior numero entre {primeiroNumero} e {segundoNumero} é: {maiorNumero} ')
print()
