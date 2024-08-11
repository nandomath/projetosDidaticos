# by nandomath
import time
from random import randint
import random

print("**************************************")
print("Bem vindo ao jogo da senha!")
print("**************************************")
print("Eu vou pensar em um número de 102 a 897")
print("e vocês vão tenatar adivinha-lo.")
print("Você vai digitar três algarismos para")
print("formar uma centena de 101 a 998,")
print("tentando acertar o meu número.")
print("Eu darei uma dica a cada centena que você falar:")
print("Um símbolo x significa algarismo errado")
print("Um símbolo o significa algarismo certo no lugar errado")
print("Um símbolo @ significa algarismo certo no lugar certo")


def leiaint():
    while True:
        n = input("Digite um algarismo de 1 a 9: ")
        if n.isnumeric():

            return int(n)

        else:
            print('\033[0;31m Voce não digitou um número válido.\033[0m')
            continue


# sorteia a senha por partes pois será preciso comparar cada algarismo
alg_cent = int(randint(1, 8))
alg_dez = int(randint(1, 9))
alg_unid = int(randint(1, 8))

senha = alg_cent * 100 + alg_dez * 10 + alg_unid
print(senha)

# recebe o palpite do jogador partes pois será preciso comparar cada algarismo
print("Você vai digitar seu palpite em três etapas:")
palpite = 000
while palpite != senha:

    primeiro_alg = leiaint()
    segundo_alg = leiaint()
    terceiro_alg = leiaint()
    palpite = primeiro_alg * 100 + segundo_alg * 10 + terceiro_alg
    print(palpite)
    tupla_senha = (alg_cent, alg_dez, alg_unid)
    tupla_palpite = (primeiro_alg, segundo_alg, terceiro_alg)

    if primeiro_alg == tupla_senha[0]:
        dica_cent = "@"
    elif primeiro_alg == tupla_senha[1]:
        dica_cent = "o"
    elif primeiro_alg == tupla_senha[2]:
        dica_cent = "o"
    else:
        dica_cent = "x"

    if segundo_alg == tupla_senha[1]:
        dica_dez = "@"
    elif segundo_alg == tupla_senha[0]:
        dica_dez = "o"
    elif segundo_alg == tupla_senha[2]:
        dica_dez = "o"
    else:
        dica_dez = "x"

    if terceiro_alg == tupla_senha[2]:
        dica_unid = "@"
    elif terceiro_alg == tupla_senha[0]:
        dica_unid = "o"
    elif terceiro_alg == tupla_senha[1]:
        dica_unid = "o"
    else:
        dica_unid = "x"

    dica = [dica_cent, dica_dez, dica_unid]
    random.shuffle(dica)

    print("Seu palpite é {} ... sua dica é ... {}{}{}".format(palpite, dica[0], dica[1], dica[2] ))

    continue

time_duration = 2.0
time.sleep(time_duration)
print("Você conseguiu acertar a senha!!! parabéns! ")
time_duration = 2.0
time.sleep(time_duration)
print("Discuta com seus colegas o que pode ter sido ")
print("feito para fazer essa previsão. Bons estudos!")
print("fim de jogo.")
time_duration = 5.0
time.sleep(time_duration)
