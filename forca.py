import random
import os
import glob

def jogar():

    imprime_mensagem_abertura()
    printa_temas()

    nome_arquivo_txt = escolha_do_tema()
    palavra_secreta = carrega_palavra_secreta(nome_arquivo_txt)
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def pede_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def escolha_do_tema():
    escolha = int(input("Escolha o tema da forca: ")) - 1
    nome_arquivo = lista_arquivos_txt()[escolha]
    print(f"O tema escolhido foi {tupla_temas()[escolha][1]}!")
    return nome_arquivo

def printa_temas():
    temas = tupla_temas()
    
    for num,tema in temas:
        print(f'({num}) {tema}')

def lista_arquivos_txt():
    arquivos_txt = glob.glob('*.txt')
    return arquivos_txt

def tupla_temas():
    temas = []

    numero_tema = 1
    for arquivo in lista_arquivos_txt():
        nome_arquivo = os.path.splitext(arquivo)[0]
        tema_maiuscula = nome_arquivo.upper()[0] + nome_arquivo[1:]
        temas.append((numero_tema, tema_maiuscula))
        numero_tema += 1
    return temas

def carrega_palavra_secreta(nome_arquivo, primeira_linha_valida=0):
    arquivo = open(nome_arquivo, "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra): 
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \\     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \\|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \\   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("\n\033[1;30;42mParabéns, você ganhou!  \033[m")
    print("\033[1;33;40m       ___________      \033[m")
    print("\033[1;33;40m      '._==_==_=_.'     \033[m")
    print("\033[1;33;40m      .-\\:      /-.     \033[m")
    print("\033[1;33;40m     | (|:.     |) |    \033[m")
    print("\033[1;33;40m      '-|:.     |-'     \033[m")
    print("\033[1;33;40m        \\::.    /       \033[m")
    print("\033[1;33;40m         '::. .'        \033[m")
    print("\033[1;33;40m           ) (          \033[m")
    print("\033[1;33;40m         _.' '._        \033[m")
    print("\033[1;33;40m        '-------'       \033[m")

def imprime_mensagem_perdedor(palavra_secreta):
    print("\n\033[1;37;41mPuxa, você foi enforcado!\033[m")
    print("\nA palavra era {}\n".format(palavra_secreta))
    print("\033[1;31;40m        _______________        \033[m")
    print("\033[1;31;40m       /               \\       \033[m")
    print("\033[1;31;40m      /                 \\      \033[m")
    print("\033[1;31;40m    //                   \\/\\   \033[m")
    print("\033[1;31;40m    \\|   XXXX     XXXX   | /   \033[m")
    print("\033[1;31;40m     |   XXXX     XXXX   |/    \033[m")
    print("\033[1;31;40m     |   XXX       XXX   |     \033[m")
    print("\033[1;31;40m     |                   |     \033[m")
    print("\033[1;31;40m     \\__      XXX      __/     \033[m")
    print("\033[1;31;40m       |\\     XXX     /|       \033[m")
    print("\033[1;31;40m       | |           | |       \033[m")
    print("\033[1;31;40m       | I I I I I I I |       \033[m")
    print("\033[1;31;40m       |  I I I I I I  |       \033[m")
    print("\033[1;31;40m       \\_             _/       \033[m")
    print("\033[1;31;40m         \\_         _/         \033[m")
    print("\033[1;31;40m           \\_______/           \033[m")

if(__name__ == "__main__"):
    jogar()
