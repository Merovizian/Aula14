print(f"\033[;1m{'Desafio 061 - Progressão Aritmética':*^70}\033[m")
razao = int(input("Informe a razao da PA: "))
termos = int(input("Informe a quantidade de termos: "))
primeiro = int(input("Informe o primeiro termo: "))
lista = ''

lista += str(primeiro) + ','

while termos > 0:
    primeiro += razao
    termos -= 1
    if termos > 1:
        lista += str(primeiro) + ','
    else:
        lista += str(primeiro) + ','
        print(lista[:len(lista) - 1])
        termos = int(input("Deseja colocar mais quantos termos (0 = nenhum): "))
        termos +=1


print(lista[:len(lista)-1])