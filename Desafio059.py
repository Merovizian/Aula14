print(f"\033[;1m{'Desafio 059 - Operações matematicas':*^70}\033[m")
import time, os
menu_escolha = 0
usuario_escolha = 4

while menu_escolha == 0:


    if usuario_escolha == 4:
        numero_a = int(input("Informe o primeiro número: "))
        numero_b = int(input("Informe o segundo número: "))

    print(f"Operações Matematicas com os números {numero_a} e {numero_b}")
    print('''    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Escolher novos numeros
    [5] - Sair do Programa''')

    usuario_escolha = int(input("Escolha uma das opções: "))


    if usuario_escolha == 1:
        print(f"{numero_a} + {numero_b} = {numero_b + numero_a}")
    if usuario_escolha == 2:
        print(f"{numero_a} x {numero_b} = {numero_a * numero_b}")
    if usuario_escolha == 3:
        if numero_a > numero_b:
            print(f"{numero_a} é o maior número")
        elif numero_b > numero_a:
            print(f"{numero_b} é o maior número")
        else:
            print(f"Os números {numero_a} e {numero_b} são iguais")
    if usuario_escolha == 5:
        menu_escolha = 1;

    time.sleep(2)
    print("\n"*100)