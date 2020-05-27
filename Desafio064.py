print(f"\033[;1m{'Desafio 064 - Somatoria de vários números':*^70}\033[m")
soma = 0
numero = 0

while numero != 999:
    soma += numero
    numero = int(input("Informe um numero: "))

print(f"A Soma dos números digitados: {soma}")
