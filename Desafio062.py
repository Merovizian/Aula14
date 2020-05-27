print(f"\033[;1m{'Desafio 061 - Progressão Aritmética':*^70}\033[m")
razao = int(input("Informe a razao da PA: "))
termos = int(input("Informe a quantidade de termos: "))
primeiro = int(input("Informe o primeiro termo: "))
lista = ''


while termos != 0:
    termos -= 1
    if termos >= 1:
        lista += str(primeiro) + ','
    else:
        lista += str(primeiro) + ','
        print(lista[:len(lista) - 1])
        termos = int(input("Deseja colocar mais quantos termos (0 = nenhum): "))

    primeiro += razao



print(lista[:len(lista)-1])