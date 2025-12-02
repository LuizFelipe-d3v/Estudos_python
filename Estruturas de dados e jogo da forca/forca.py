print("*********************************")
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')

palavra_secreta = 'banana'

print("A palavra secreta possui {} letras".format(len(palavra_secreta)))

acertou = False
errou = False
while not acertou and not errou:
    chute = input("Digite uma letra: ")

    if chute in palavra_secreta:
        print("Você acertou uma letra!")
    else:
        print("Você errou!")

