from tkinter import *     # by nandomath
from random import *


def aviso1():
    mensagem1["text"] = "Pense em um número e anote!"


valor_1 = 3
rand1 = int(randint(2, 6))


def aviso2():
    mensagem2["text"] = f"Multiplique o seu número por {rand1}"


valor_2 = valor_1 * rand1
k = randint(2, 5) * rand1


def aviso3():
    mensagem3["text"] = f"Adicione o valor {k} ao resultado que vc encontrou. "


valor_3 = valor_2 + k


def aviso4():
    mensagem4["text"] = "Espero que vc tenha escolhido um número pequeno! kkk "


def aviso5():
    mensagem5["text"] = f"Divida esse resultado  por {rand1}"


valor_4 = valor_3 / rand1


def aviso6():
    mensagem6["text"] = "Agora subtraia o número que você pensou la no início."


valor_5 = int(valor_4 - valor_1)


def aviso7():
    mensagem7["text"] = f"O resultado que você encontrou é {valor_5}"


tela1 = Tk()

tela1.title("Adivinha o resultado")
tela1.geometry("420x540+100+100")

msg1 = Label(tela1, text="\n Bem vindo ao desafio: Adivinhando o resultado!\n"
                         "\n Você vai escolher um número e depois de você  fazer"
                         "\n algumas contas eu direi o resultado da conta"
                         "\n que você fez! Clique no 1° passo para começar!")
msg1["font"] = ("Verdana", "10", "bold")
msg1.pack()

mensagem1 = Label(tela1, text="", font="arial 10 bold")
mensagem1.pack()
bt_aviso1 = Button(tela1, command=aviso1, text="1° passo:", font="Calibri  10", width=8)
bt_aviso1.pack()

mensagem2 = Label(tela1, text="", font="arial 10 bold")
mensagem2.pack()
bt_aviso2 = Button(tela1, command=aviso2, text="2° passo:", font="Calibri  10", width=8)
bt_aviso2.pack()

mensagem3 = Label(tela1, text="", font="arial 10 bold")
mensagem3.pack()
bt_aviso3 = Button(tela1, command=aviso3, text="3° passo:", font="Calibri  10", width=8)
bt_aviso3.pack()

mensagem4 = Label(tela1, text="", font="arial 10 bold")
mensagem4.pack()
bt_aviso4 = Button(tela1, command=aviso4, text="4° passo:", font="Calibri  10", width=8)
bt_aviso4.pack()

mensagem5 = Label(tela1, text="", font="arial 10 bold")
mensagem5.pack()
bt_aviso5 = Button(tela1, command=aviso5, text="5° passo:", font="Calibri  10", width=8)
bt_aviso5.pack()

mensagem6 = Label(tela1, text="", font="arial 10 bold")
mensagem6.pack()
bt_aviso6 = Button(tela1, command=aviso6, text="6° passo:", font="Calibri  10", width=8)
bt_aviso6.pack()

mensagem7 = Label(tela1, text="", font="arial 10 bold")
mensagem7.pack()
bt_aviso7 = Button(tela1, command=aviso7, text="7° passo:", font="Calibri" "10", width=8)
bt_aviso7.pack()

mensagem_final = Label(tela1, text="\nAgora discuta com seus colegas o que pode ter sido feito"
                                   "\n para fazer essa previsão. Bons estudos!", font="arial 10 bold")
mensagem_final.pack()

bt_sair = Button(tela1, command=tela1.quit, text="Sair", font="Calibri" "10", width=8)
bt_sair.pack()
tela1.mainloop()
