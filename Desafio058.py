import random, time
print(f"\033[;1m{'Desafio 058 - Jogo Adivinhação entre 0 e 10':*^70}")
nivel = int(input("Escolha um nivel de dificuldade(1 a 5): "))
score = 5*nivel
fim = 0
print(f"Nivel {nivel} - Escolha um numero entre 1 e {nivel * 5}")

while fim == 0 and score > 0:
    escolha = int(input("Digite a sua aposta: "))
    print("\033[0;32mComputador jogando..\033[m")
    time.sleep(0.5)
    escolha_pc = random.randrange(1, (nivel*5)+1)
    print(f"\033[1;34mO computador escolheu: {escolha_pc}\033[m")
    time.sleep(0.5)

    if escolha_pc == escolha:
        fim = 1;
    else:
        score -= 1
        print(f"\033[1;31mErrou, Tente de novo!\033[m")

time.sleep(1)
if score > 0:
    print(f"Fim do jogo!! seu score foi de {score} pontos")
else:
    print(f"Você não conseguiu ganhar!")
