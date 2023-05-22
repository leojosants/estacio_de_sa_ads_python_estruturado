try:
    num = eval(input("\nEntre com um número inteiro: "))
    print(num)
except ValueError:
    print("Mensagem 1 \n")
except IndexError:
    print("Mensagem 2 \n")
except:
    print("Mensagem 3 \n")
