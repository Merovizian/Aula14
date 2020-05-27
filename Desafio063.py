print(f"\033[;1m{'Desafio 063 - Sequência de Fibonacci':*^70}\033[m")
numero = int(input("Informe a quantidade de termos: "))
antes = 0
depois = 1
soma = 0
list = str(soma) + ','

while numero > 1:
    if antes == 0:
        soma = 1
    else:
        soma = antes + depois

    depois = antes
    antes = soma


    numero -= 1
    list += str(soma) + ','

print(list[:len(list)-1])