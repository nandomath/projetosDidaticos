print("**************************************")
print("Bem vindo ao desafio: Adivinhe a soma!")
print("**************************************")
print("Você vai digitar três centenas de 101 a 899,")
print("apenas números naturais e eu digitarei")
print("duas, no final vamos somar tudo.")
print("Mas quando você digitar o primeiro número eu")
print("ja falarei o resultado da soma de todos os")
print("cinco números,ok? Pronto? Então vamos lá!")
import time
primeiro_num = 100
while primeiro_num < 101 or primeiro_num > 899:
    numero1_str = input("digite o primeiro número:")
    print("você digitou:", numero1_str)

    time_duration = 1.0
    time.sleep(time_duration)
    primeiro_num = int(numero1_str)
    if primeiro_num < 101 or primeiro_num > 899:
        print("O seu número tem que estar entre 101 e 899.")
        continue

    resultado_final_str = primeiro_num + 1998
    print("O resultado será:", resultado_final_str)
    time_duration = 1.0
    time.sleep(time_duration)

segundo_num = 100
while segundo_num < 101 or segundo_num > 899:
    print("Agora você digita o segundo número")
    numero2_str = input("digite o segundo número:")
    print("você digitou", numero2_str)

    time_duration = 1.0
    time.sleep(time_duration)

    segundo_num = int(numero2_str)
    if segundo_num < 101 or segundo_num > 899:
        print("O seu número tem que estar entre 101 e 899.")
        continue

print("Agora eu digito o terceiro número")

time_duration = 1.0
time.sleep(time_duration)

numero3_str = 999 - segundo_num
print("Eu digitei", numero3_str)

time_duration = 2.0
time.sleep(time_duration)

terceiro_num = int(numero3_str)

quarto_num = 100
while quarto_num < 101 or quarto_num > 899:
    print("Agora você digita o quarto número")
    numero4_str = input("digite o quarto número:")
    print("você digitou", numero4_str)

    time_duration = 1.0
    time.sleep(time_duration)

    quarto_num = int(numero4_str)
    if quarto_num < 101 or quarto_num > 899:
        print("O seu número tem que estar entre 101 e 899.")
        continue

print("Agora eu digito o quinto e último número")

time_duration = 1.0
time.sleep(time_duration)

numero5_str = 999 - quarto_num
print("Eu digitei", numero5_str)

time_duration = 2.0
time.sleep(time_duration)

quinto_num = int(numero5_str)

print("Agora faça a conta com todos os números")
print("e veremos se eu acertei o resultado.")

time_duration = 2.0
time.sleep(time_duration)

print("Seu 1° número:", numero1_str)
print("Seu 2° número:", numero2_str)
print("Meu 3° número:", numero3_str)
print("Seu 4° número:", numero4_str)
print("Meu 5° número:", numero5_str)
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
print("fim de jogo.")

time_duration = 5.0
time.sleep(time_duration)