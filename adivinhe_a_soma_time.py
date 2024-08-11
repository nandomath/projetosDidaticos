# by nandomath
import time

print("**************************************")
print("Bem vindo ao desafio: Adivinhe a soma!")
print("**************************************")
print("Você vai digitar três centenas de 101 a 899,")
print("apenas números naturais e eu digitarei")
print("duas, no final vamos somar tudo.")
print("Mas quando você digitar o primeiro número eu")
print("ja falarei o resultado da soma de todos os")
print("cinco números,entendido? Então vamos lá!")


def leiaint():
    while True:
        n = input("Digite um numero: ")
        if n.isnumeric():

            return int(n)

        else:
            print('\033[0;31m Voce não digitou um numero.\033[0m')
            continue


primeiro_num = 100
while primeiro_num < 101 or primeiro_num > 899:
    primeiro_num = leiaint()
    print("você digitou:", primeiro_num)

    time_duration = 1.0
    time.sleep(time_duration)

    if primeiro_num < 101 or primeiro_num > 899:
        print("\033[0;31m O seu número tem que estar entre 101 e 899. \033[0m")

        continue

    resultado_final = primeiro_num + 1998
    print("O resultado será:", resultado_final)

    time_duration = 1.0
    time.sleep(time_duration)

segundo_num = 100
while segundo_num < 101 or segundo_num > 899:
    print("Agora você digita o segundo número")
    numero2 = leiaint()
    print("você digitou", numero2)

    time_duration = 1.0
    time.sleep(time_duration)

    segundo_num = numero2
    if segundo_num < 101 or segundo_num > 899:
        print("\033[0;31m O seu número tem que estar entre 101 e 899. \033[0m")
        continue

print("Agora eu digito o terceiro número")

time_duration = 1.0
time.sleep(time_duration)

numero3 = 999 - segundo_num
print("Eu digitei", numero3)

time_duration = 2.0
time.sleep(time_duration)

terceiro_num = int(numero3)

quarto_num = 100
while quarto_num < 101 or quarto_num > 899:
    print("Agora você digita o quarto número")
    numero4 = leiaint()
    print("você digitou", numero4)

    time_duration = 1.0
    time.sleep(time_duration)

    quarto_num = numero4
    if quarto_num < 101 or quarto_num > 899:
        print("\033[0;31m O seu número tem que estar entre 101 e 899. \033[0m")
        continue

print("Agora eu digito o quinto e último número")

time_duration = 1.0
time.sleep(time_duration)

numero5 = 999 - quarto_num
print("Eu digitei", numero5)

time_duration = 2.0
time.sleep(time_duration)

quinto_num = int(numero5)

print("Agora faça a soma de todos os números")
print("e veremos se eu acertei o resultado.")

time_duration = 2.0
time.sleep(time_duration)

print("Seu 1° número:", primeiro_num)
print("Seu 2° número:", numero2)
print("Meu 3° número:", numero3)
print("Seu 4° número:", numero4)
print("Meu 5° número:", numero5)
print("_____________+_____")
total = primeiro_num + segundo_num + terceiro_num + quarto_num + quinto_num
print("_____________", total)

time_duration = 2.0
time.sleep(time_duration)

print("Eu acertei ! HAHA!!")

time_duration = 1.0
time.sleep(time_duration)

print("Discuta com seus colegas o que pode ter sido ")
print("feito para fazer essa previsão. Bons estudos!")

time_duration = 5.0
time.sleep(time_duration)
