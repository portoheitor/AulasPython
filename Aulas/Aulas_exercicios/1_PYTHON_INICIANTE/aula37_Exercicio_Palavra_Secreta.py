'''
Faça um joqo para o usuario adivinhar qual a palavra secreta.

- Voce vai propor uma palavra secreta qualquer e vai dar 
    a possibilidade para o usuario digitar apenas uma letra.
    
- Quando o usuario digitar uma letra, voce vai conferir se a letra
    digitada esta na palavra secreta

        - Se a letra digitada estiver na palavra secreta; exiba a letra;
        - Se a letra digitada nao estiver na palavra secreta exiba '*';
    
- Faca a contagem de tentativas do seu usuario.

'''
 

import random

def escolher_palavra():
    palavras = ["python", "computador", "programacao", "tecnologia", "heitor", "maite"]
    return random.choice(palavras)

def verificar_letra(letra, palavra_secreta, letras_corretas):
    if letra in palavra_secreta:
        letras_corretas.append(letra)
        return True
    else:
        return False

def exibir_palavra(palavra_secreta, letras_corretas):
    for letra in palavra_secreta:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("*", end=" ")
    print()

def jogar():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 0

    print("Bem-vindo ao jogo da Forca!")
    print("A palavra secreta tem", len(palavra_secreta), "letras.")
    exibir_palavra(palavra_secreta, letras_corretas)

    while True:
        tentativa = input("Digite uma letra: ").lower()
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        tentativas += 1
        if verificar_letra(tentativa, palavra_secreta, letras_corretas):
            print("Letra correta!")
        else:
            print("Letra incorreta!")

        exibir_palavra(palavra_secreta, letras_corretas)

        if all(letra in letras_corretas for letra in palavra_secreta):
            print(f'Parabéns, você acertou a palavra secreta "{palavra_secreta}" em {tentativas} tentativas!')
            break

# Jogo so executa se o arquivo for executado diretamente, evita que caso seja importado(modulo) execute sem 'querer'
if __name__ == "__main__":
    jogar()
