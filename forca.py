def jogar():   
    import random
    bem_vindo = "Bem vindo ao jogo da forca"

    print("\n")
    print("*"*40)
    print(bem_vindo.center(40))
    print("*"*40)

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]


    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Informe a letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

        

            


if (__name__ == "__main__"):
    jogar()