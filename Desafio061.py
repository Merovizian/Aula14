print(f"\033[;1m{'Desafio 061 - Progressão Aritmética':*^70}\033[m")
razao = int(input("Informe a razao da PA: "))
termos = int(input("Informe a quantidade de termos: "))
primeiro = int(input("Informe o primeiro termo: "))

print(primeiro,end=',')
while termos > 1:
    primeiro += razao
    termos -= 1
    print(f"{primeiro}," if termos > 1 else f"{primeiro}",end = '')
