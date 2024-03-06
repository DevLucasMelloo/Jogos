import adivinhacao
import forca

def escolhe_o_jogo():
    print("**************************************************")
    print("Escolha o jogo!")
    print("**************************************************")

    print("(1) Adivinhação (2) Forca")

    jogo = int(input("Escolha o jogo: "))

    if(jogo == 1):
        print("Jogo da Adivinhação")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogo da Forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolhe_o_jogo()