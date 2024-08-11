# by nandomath

from tkinter import *
from random import *


def aviso1():
    mensagem1["text"] = "Pense em um número e anote!"


valor_1 = 3
rand1 = int(randint(2, 6))


def aviso2():
    mensagem2["text"] = "Multiplique o seu número por {}".format(rand1)


valor_2 = valor_1 * rand1
k = randint(2, 5) * rand1


def aviso3():
    mensagem3["text"] = "Adicione o valor {} ao resultado que vc encontrou. ".format(k)


valor_3 = valor_2 + k


def aviso4():
    mensagem4["text"] = "Espero que vc tenha escolhido um número pequeno! kkk "


def aviso5():
    mensagem5["text"] = "Divida esse resultado  por {}".format(rand1)


valor_4 = valor_3 / rand1


def aviso6():
    mensagem6["text"] = "Agora subtraia o número que você pensou la no início."


valor_5 = int(valor_4 - valor_1)


def aviso7():
    mensagem7["text"] = "O resultado que você encontrou é {}".format(valor_5)


tela1 = Tk()

# Título da janela
tela1.title("Adivinha o resultado")
tela1.geometry("360x540+100+100")

# primeira mensagem ao usuário
msg = Label(tela1, text="Bem vindo ao desafio de adivinhar o resultado!")
msg["font"] = ("Verdana", "10", "italic", "bold")
msg.pack()

# segunda mensagem ao usuário
msg2 = Label(tela1, text="Depois de você fazer algumas contas "
                         "\n eu direi o resultado da conta que você fez!")
msg2["font"] = ("Verdana", "10")
msg2.pack()

# isso aqui abaixo é palhaçada
mensagem_so_pra_dar_um_espaco = Label(tela1, text="", font="arial 10 bold")
mensagem_so_pra_dar_um_espaco.pack()

# botão aviso1
mensagem1 = Label(tela1, text="", font="arial 10 bold")
mensagem1.pack()
aviso1 = Button(tela1, command=aviso1)
aviso1["text"] = "1° passo:"
aviso1["font"] = ("Calibri", "10")
aviso1["width"] = 8
aviso1.pack()

# botão aviso2
mensagem2 = Label(tela1, text="", font="arial 10 bold")
mensagem2.pack()
aviso2 = Button(tela1, command=aviso2)
aviso2["text"] = "2° passo:"
aviso2["font"] = ("Calibri", "10")
aviso2["width"] = 8
aviso2.pack()

# botão aviso3
mensagem3 = Label(tela1, text="", font="arial 10 bold")
mensagem3.pack()
aviso3 = Button(tela1, command=aviso3)
aviso3["text"] = "3° passo:"
aviso3["font"] = ("Calibri", "10")
aviso3["width"] = 8
aviso3.pack()

# botão aviso4
mensagem4 = Label(tela1, text="", font="arial 10 bold")
mensagem4.pack()
aviso4 = Button(tela1, command=aviso4)
aviso4["text"] = "4° passo:"
aviso4["font"] = ("Calibri", "10")
aviso4["width"] = 8
aviso4.pack()

# botão aviso5
mensagem5 = Label(tela1, text="", font="arial 10 bold")
mensagem5.pack()
aviso5 = Button(tela1, command=aviso5)
aviso5["text"] = "5° passo:"
aviso5["font"] = ("Calibri", "10")
aviso5["width"] = 8
aviso5.pack()

# botão aviso6
mensagem6 = Label(tela1, text="", font="arial 10 bold")
mensagem6.pack()
aviso6 = Button(tela1, command=aviso6)
aviso6["text"] = "6° passo:"
aviso6["font"] = ("Calibri", "10")
aviso6["width"] = 8
aviso6.pack()

# botão aviso7
mensagem7 = Label(tela1, text="", font="arial 10 bold")
mensagem7.pack()
aviso7 = Button(tela1, command=aviso7)
aviso7["text"] = "7° passo:"
aviso7["font"] = ("Calibri", "10")
aviso7["width"] = 8
aviso7.pack()

# mensagem final
mensagem_final = Label(tela1, text="Agora discuta com seus colegas o que pode ter sido feito"
                                   "\n para fazer essa previsão. Bons estudos!", font="arial 10 bold")
mensagem_final.pack()

# botão Sair
sair = Button(tela1)
sair["text"] = "Sair"
sair["font"] = ("Calibri", "10")
sair["width"] = 5
sair["command"] = tela1.quit
sair.pack()

tela1.mainloop()
