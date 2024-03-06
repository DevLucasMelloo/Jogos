import random

def jogar():
    imprime_mensagem_abertura()
    palavra_chave = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_chave)

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):

        chute = pede_chute()

        if(chute in palavra_chave):
            marca_chute_correto(chute, letras_acertadas, palavra_chave)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        mensagem_vencedora()
    else:
        mensagem_perdedora(palavra_chave)
    print("Fim de jogo!")

def imprime_mensagem_abertura():
    print("**************************************************")
    print("Bem vindo ao jogo da forca, tente adivinhar se puder!")
    print("**************************************************")
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavra = []

    for linha in arquivo:  # laço para acessar cada linha dentro do arquivo
        linha = linha.strip()  # remover espaços dentro da lista
        palavra.append(linha)  # adicionar palavras na lista

    arquivo.close()

    numero = random.randrange(0,len(palavra))  # randomizar a escolha de palavras do 0 até o fim, caso terminasse em numero esse numero seria excluido
    palavra_chave = palavra[numero].upper()  # randomizar a palavra da lista que sera escolhida
    return palavra_chave

def inicializa_letras_acertadas(palavra_chave):
    return ["_" for letra in palavra_chave] #tradução: usar no caracter a letra da palavra chave

def pede_chute():
    chute = input("Escolha uma letra : ")
    chute = chute.strip().upper()  # remover os espaços no chute e upper deixar maiusculo
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_chave):
    index = 0
    for letra in palavra_chave:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1  # index = index + 1, msm coisa escrita diferente

def mensagem_vencedora():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedora(palavra_chave):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_chave))

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()