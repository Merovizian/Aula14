print(f"\033[;1m{'Desafio 057 - é H ou M':*^70}\033[m")
sexo = ' '
tentativas = 0
while sexo != 'f' and sexo != 'F' and sexo != 'm' and sexo != 'M':
    if tentativas > 0:
        print(f"\033[1;31m'{sexo}' não é um valor correto, por favor informe novamente!\033[m")
    sexo = str(input("Diga o seu sexo: "))
    tentativas += 1


