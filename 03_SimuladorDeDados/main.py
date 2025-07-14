import random

def rolar_dados(total: int = 2) -> list[int]:
    if total <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for _ in range(total):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls

def main():
    while True:
        try:
            user_input: str = input("Quantos dados você gostaria de jogar? (ou digite 'sair' para encerrar): ")

            if user_input.lower() in ['sair', 'exit']:
                print("Obrigado por jogar!")
                break

            print("Você rolou:", rolar_dados(int(user_input)))

        except ValueError:
            print("Por favor, entre com um número válido!")

if __name__ == "__main__":
    main()
