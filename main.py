from functions import *

print("Iniciando o QUIZ do HenriqueKKKKKKK")
iniciar = pedir_iniciar_quiz()

if iniciar == 'S':
    score = 0
    total_perguntas = 0
    print("Iniciando...")

    perguntas = carregar_perguntas('perguntas.json')

    for i, pergunta in enumerate(perguntas, start=1):
        total_perguntas += 1
        print(f"{i}- {pergunta['pergunta']}")
        for opcao in pergunta['opcoes']:
            print(opcao)
        
        resposta_usuario = input("Digite a resposta correta: ").upper()
        score = VerificarRespostas(pergunta['resposta_correta'], resposta_usuario, score)
        print(f"Seu score atual é: {score}")


    print(f"\nVocê acertou {score} de {total_perguntas} perguntas.")
    print(f"Você errou {total_perguntas - score} perguntas.")

else:
    print("Saindo do QUIZ...")
