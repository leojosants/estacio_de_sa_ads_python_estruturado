"""
    Implementar uma solução em Python que resolva a seguinte questão:
        - Se nota for maior ou igual a 7, o estudante foi aprovado.
        - Se nota for menor que 7 e maior ou igual a 5, o estudante está em recuperação.
        - Se nota for menor que 5, o estudante está reprovado.
"""

print()

nota = 43.5
situacao = 'Situação indefinida'

if(nota < 5.0):
    situacao = 'Reprovado'

elif(nota >= 5.0 and nota < 7):
    situacao = 'Recuperação'

else:
    situacao = 'Aprovado'


print(f'Situação do aluno: {situacao}')
print()
