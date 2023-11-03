import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "desenvolvimento", "computador", "inteligencia"]

# Função para escolher uma palavra aleatória da lista
def escolher_palavra():
    return random.choice(palavras)

# Função para exibir o estado atual da palavra, com letras adivinhadas
def mostrar_palavra(palavra, letras_adivinhadas):
    resultado = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

# Função principal do jogo
def jogo_da_forca():
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6  # Número máximo de tentativas antes de perder o jogo

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta. A palavra tem", len(palavra_secreta), "letras.")

    while tentativas > 0:
        palavra_atual = mostrar_palavra(palavra_secreta, letras_adivinhadas)
        print("\nPalavra atual: " + palavra_atual)

        letra = input("Digite uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já adivinhou esta letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            letras_adivinhadas.append(letra)
            if palavra_atual == palavra_secreta:
                print("\nParabéns! Você adivinhou a palavra corretamente: " + palavra_secreta)
                break
        else:
            letras_adivinhadas.append(letra)
            tentativas -= 1
            print("\nLetra errada. Você tem", tentativas, "tentativas restantes.")

    if tentativas == 0:
        print("\nFim de jogo! Você perdeu. A palavra secreta era: " + palavra_secreta)

if __name__ == "__main__":
    jogo_da_forca()
