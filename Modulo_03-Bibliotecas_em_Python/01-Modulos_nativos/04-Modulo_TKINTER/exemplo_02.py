from tkinter import *


def funcClicar():
    print("Botão pressionado")


janelaPrincipal = Tk()
texto = Label(master=janelaPrincipal, text="Minha janela exibida")
texto.pack()

""" Criação do objeto Label para conter a imagem e seu posicionamento.  """
pic = PhotoImage(file="logoEstacio.gif")
logo = Label(master=janelaPrincipal, image=pic)
logo.pack() #   Coloca o elemento centralizado e posicionado o mais perto possível do topo, depois dos elementos posicionados anteriormente.

botao = Button(master=janelaPrincipal, text='Clique', command=funcClicar)
botao.pack()

janelaPrincipal.mainloop()
