#

escolha = input("\nEscolha uma opção de função [1 ou 2]: ")

if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)

else:
    def func2(x):
        return x + 2
    s = func2(10)

print(f'{s}\n')
