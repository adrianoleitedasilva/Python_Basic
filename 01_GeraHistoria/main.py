import random

# Modelos básicos de personagens e cenários
personagens = [
    {"nome": "Luna", "tipo": "princesa", "personalidade": "curiosa e corajosa"},
    {"nome": "Theo", "tipo": "camponês", "personalidade": "gentil e sonhador"},
    {"nome": "Zara", "tipo": "feiticeira", "personalidade": "inteligente e misteriosa"},
    {"nome": "Leo", "tipo": "aprendiz de cavaleiro", "personalidade": "valente e atrapalhado"},
]

cenarios = [
    "num reino encantado escondido entre as montanhas azuis",
    "em uma floresta mágica onde os animais falam",
    "em uma vila flutuante sobre nuvens de algodão",
    "no fundo do mar, entre corais brilhantes e criaturas mágicas",
]

problemas = [
    "um feitiço antigo começou a apagar as cores do mundo",
    "o tempo parou e ninguém mais conseguia se mover",
    "o cristal da alegria foi roubado do castelo",
    "um dragão adormeceu e seus sonhos causavam terremotos mágicos",
]

# Função para gerar uma conversa entre os dois personagens
def gerar_conversa(p1, p2):
    falas_p1 = [
        f"{p1['nome']}: Você também sentiu isso? Algo estranho está acontecendo!",
        f"{p1['nome']}: Precisamos fazer alguma coisa. Não podemos deixar isso assim.",
        f"{p1['nome']}: Eu tenho uma ideia... mas é meio arriscada.",
    ]

    falas_p2 = [
        f"{p2['nome']}: Eu senti sim! Foi como se o vento tivesse parado de soprar.",
        f"{p2['nome']}: Estou com você. Vamos resolver isso juntos.",
        f"{p2['nome']}: Uma ideia arriscada é melhor do que nenhuma ideia!",
    ]

    conversa = ""
    for i in range(3):
        conversa += falas_p1[i] + "\n"
        conversa += falas_p2[i] + "\n"
    return conversa

# Função principal para montar a história
def gerar_historia():
    p1, p2 = random.sample(personagens, 2)
    cenario = random.choice(cenarios)
    problema = random.choice(problemas)

    historia = f"Era uma vez, {cenario}.\n"
    historia += f"Lá vivia {p1['nome']}, um(a) {p1['tipo']} {p1['personalidade']}.\n"
    historia += f"E também {p2['nome']}, um(a) {p2['tipo']} {p2['personalidade']}.\n\n"
    historia += f"Um dia, {problema}.\n"
    historia += "Então, os dois decidiram conversar:\n\n"
    historia += gerar_conversa(p1, p2)
    historia += "\nE foi assim que começou a aventura mais incrível de todas!"

    return historia

# Executa a função
print(gerar_historia())
