# Jogo da forca python3 - Para rodar no terminal escreva "python3 forca.py"

import random


def palavra():
    PALAVRAS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
    sortear_palavra = random.choice(PALAVRAS)
    palavra = sortear_palavra
    print (palavra)
    return palavra


def desenho(erros):
    if erros == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    
    elif erros == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    
    elif erros == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /| ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()

    elif erros == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()

    elif erros == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()

    elif erros == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   /  ")
        print("_      ")
        print()

    elif erros == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\ ")
        print("|    | ")
        print("|   / \ ")
        print("_      ")
        print("FORCA!")
        print()

perguntarNovamente = True
game_on = True
while game_on:
    palavra_secreta = palavra()
    palavra_secreta_list = [letra for letra in palavra_secreta]
    chances = 6
    tentativas = []
    erros = 0
    #Esconder palavra
    for i in range(101):
        print()
    # Comentar a linha abaixo quando não for teste.
    print (palavra_secreta_list)
    #Começo do jogo
    while perguntarNovamente:
        print("A palavra:","_ "*len(palavra_secreta_list))
        desenho(erros)
        if erros == 6:
            perguntarNovamente = False
            game_on = False
            break
        chute = input("Digite uma letra(ou a palavra): ")
        if chute == palavra_secreta:
            print("Parabéns você acertou!!")
            break
        elif chute not in(palavra_secreta_list):
            if chute in(tentativas):
                print("Você já tentou essa letra!")
                continue
            else:
                print("Não há essa letra na palavra!")
                tentativas.append(chute)
                erros +=1
                continue
        else:
            print("Você acertou uma letra!")
            tentativas.append(chute)
            continue
        
