print(f"\033[;1m{'Desafio 060 - Fatorial':*^70}\033[;m")
numero = int(input("Escolha um numero para o fatorial: "))
n = 0
soma = 1
print (f"{numero}! = ",end = '')
while n < numero:
    print(f"{numero-n}",end="")
    n += 1
    print(f"x" if n < numero else "",end = '')
    soma *= n


print(f' = {soma}')