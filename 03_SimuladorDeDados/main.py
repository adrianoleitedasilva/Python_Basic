import random

def rolar_dados(total: int = 2) -> list[int]:
    if total <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range(total):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls

def main():
    while True:
        try:
            user_imput: str = input('Quantos dados você gostaria de jogar?')

            if user_imput.lower() == 'exit':
                print("Obrigado por jogar!")
                break
            print(rolar_dados(int(user_imput)))
        except ValueError:
            print("(Por favor, entre com um valor válido!)")


if __name__ == "__main__":
    main()