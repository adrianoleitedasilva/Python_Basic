import random

def obter_nome():
    nome = input("Olá! Qual é o seu nome? ")
    print(f"Bem-vindo ao jogo da forca, {nome}!\n")
    return nome

def escolher_palavra(lista_palavras):
    return random.choice(lista_palavras)

def mostrar_palavra_oculta(palavra, letras_certas):
    return ' '.join([letra if letra in letras_certas else '_' for letra in palavra])

def jogar_forca(palavra):
    tentativas = 3
    letras_certas = set()
    letras_erradas = set()

    while tentativas > 0:
        print("\nPalavra:", mostrar_palavra_oculta(palavra, letras_certas))
        palpite = input("Digite uma letra (ou 'sair' para encerrar): ").lower()

        if palpite == "sair":
            return "sair"

        if len(palpite) != 1 or not palpite.isalpha():
            print("Digite apenas UMA letra válida.")
            continue

        if palpite in letras_certas or palpite in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if palpite in palavra:
            print("Boa! Você acertou uma letra.")
            letras_certas.add(palpite)
        else:
            print("Letra errada.")
            letras_erradas.add(palpite)
            tentativas -= 1
            print(f"Você ainda tem {tentativas} tentativa(s).")

        if all(letra in letras_certas for letra in palavra):
            print("\nParabéns! Você acertou a palavra:", palavra)
            return True

    print("\nSuas tentativas acabaram. A palavra era:", palavra)
    return False

def main():
    lista_palavras = [
        "python", "magia", "dragao", "castelo", "espada",
        "heroi", "feitico", "aventura", "vilao", "missao"
    ]

    nome = obter_nome()
    pontuacao = 0

    while True:
        palavra = escolher_palavra(lista_palavras)
        resultado = jogar_forca(palavra)

        if resultado == "sair":
            break
        elif resultado is True:
            pontuacao += 1

    print(f"\nObrigado por jogar, {nome}! Você acertou {pontuacao} palavra(s). Até a próxima!")

if __name__ == "__main__":
    main()
