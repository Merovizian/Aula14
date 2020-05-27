print(f"\033[;1m{'Desafio 065 - Média , Maior , Menor entre vários números':*^70}\033[m")
soma = 0
maior = 0
continuar = 0
contador = 0

while continuar == 0:
    numero = int(input("Digite um número: "))

    if contador == 0:
        menor = numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    soma += numero
    contador += 1

    if (input("Deseja continuar (S/N): ")).upper() == 'N':
        continuar = 1

print(f"A média dos {contador} números digitados é {soma/contador}")
print(f"O maior numero é o {maior} e o menor é o {menor}")