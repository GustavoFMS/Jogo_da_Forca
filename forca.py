def jogar():   
    import random
    bem_vindo = "Bem vindo ao jogo da forca"

    print("\n")
    print("*"*40)
    print(bem_vindo.center(40))
    print("*"*40)

    palavra_secreta = "banana".upper()
    letras_acertadas = []
    for letra in palavra_secreta:
        letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0 

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Informe a letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros = erros + 1

        enforcou = erros == 6 
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        print("Voce ganhou!!")
    else: 
        print("Voce perdeu :(")
if (__name__ == "__main__"):
    jogar()