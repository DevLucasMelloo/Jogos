import random

def jogar():
    print("***********************************************************")
    print("Bem vindo ao jogo da adivinhação, tente adivinhar se puder!")
    print("***********************************************************")

    numero_secreto = random.randrange(1,51)
    tentativas_de_chutes = 0
    pontos = 100

    print("Escolha o nivel de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha o nivel do jogo: "))

    if(nivel == 1):
        tentativas_de_chutes = 20
    elif(nivel == 2):
        tentativas_de_chutes = 10
    else:
        tentativas_de_chutes = 5

    for rodada in range(1, tentativas_de_chutes + 1):
        print("Tentativa {} de {}".format(rodada, tentativas_de_chutes))
        chute = input("Digite um número de 1 a 50: ")
        print("Voce digitou ", chute)
        chute = int(chute)

        if(chute < 1 or chute > 50):
            print("Você deve digitar um valor entre 1 e 50")
            continue

        acertou = chute == numero_secreto
        errou_para_mais = chute > numero_secreto
        errou_para_menos = chute < numero_secreto

        if(acertou):
            print("Correto, você ganhou com uma pontuação de {} pontos!".format(pontos))
            break
        else:
            if(errou_para_mais):
                print("Errado, o seu número é maior que o número correto")
            elif(errou_para_menos):
                print("Errado, o seu número é menor que o número correto")
                pontos_perdido = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdido

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()