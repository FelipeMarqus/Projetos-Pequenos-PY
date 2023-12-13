# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '2',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '0',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '1',
    },
]
pergunta_0 = perguntas[0]['Pergunta']
pergunta_1 = perguntas[1]['Pergunta']
pergunta_2 = perguntas[2]['Pergunta']

resposta_0 = int(perguntas[0]['Resposta'])
resposta_1 = int(perguntas[1]['Resposta'])
resposta_2 = int(perguntas[2]['Resposta'])

acertos = 0
contavel = 0

while True:
    
#  PERGUNTA 0

    print(f'Pergunta: {pergunta_0} ')
    print()
    print(f'Opções:')
    
    for opcao in perguntas[0]['Opções']:
        print(f'{contavel})  {opcao}')
        contavel += 1

    resposta_digitada_0 = int(input("Escolha uma Opção:  "))

    if resposta_digitada_0 == resposta_0:
        print("Acertou 😊")
        print()
        acertos += 1
    else:
        print("Errou Feio 😒")
        print()

#  PERGUNTA 1

    print(f'Pergunta: {pergunta_1} ')
    print()
    print(f'Opções:')

    contavel = 0
    
    for opcao in perguntas[1]['Opções']:
        print(f'{contavel})  {opcao}')
        contavel += 1

    resposta_digitada_1 = int(input("Escolha uma Opção:  "))

    if resposta_digitada_1 == resposta_1:
        print("Acertou 😊")
        print()
        acertos += 1
    else:
        print("Errou Feio 😒")
        print()

#  PERGUNTA 2
    print(f'Pergunta: {pergunta_2} ')
    print()
    print(f'Opções:')

    contavel = 0
    
    for opcao in perguntas[2]['Opções']:
        print(f'{contavel})  {opcao}')
        contavel += 1

    resposta_digitada_2 = int(input("Escolha uma Opção:  "))

    if resposta_digitada_2 == resposta_2:
        print("Acertou 😊")
        print()
        acertos += 1
        break
    else:
        print("Errou Feio 😒")
        print()
        break

print(f'Você acertou {acertos} \nde 3 perguntas.')