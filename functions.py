def AcaoAcertar():
    print("Executando uma ação especial para resposta correta!")

def VerificarRespostas(resposta_correta, resposta_usuario, score):
    if resposta_usuario == resposta_correta:
        print("Você Acertou!!")
        score += 1
        AcaoAcertar()
    else:
        print("Você Errou!!")
    return score

def pedir_iniciar_quiz():
    iniciar = input("Deseja iniciar o QUIZ? (S/N): ").upper()
    
    while iniciar not in ['S', 'N']:
        print("Entrada inválida! Digite 'S' para sim ou 'N' para não.")
        iniciar = input("Deseja iniciar o QUIZ? (S/N): ").upper()
    
    return iniciar

print("Iniciando o QUIZ do HenriqueKKKKKKK")
iniciar = pedir_iniciar_quiz()

if iniciar == 'S':
    score = 0
    total_perguntas = 0
    print("Iniciando...")

    perguntas = [
        {
            "pergunta": "Que Empresa Desenvolveu o jogo GTA V?",
            "opcoes": ["A) Rockstar Games", "B) Ubisoft", "C) EA Games", "D) Activision"],
            "resposta_correta": 'A'
        },
        {
            "pergunta": "Qual o nome do protagonista do jogo The Legend of Zelda?",
            "opcoes": ["A) Zelda", "B) Link", "C) Ganondorf", "D) Hylia", "E) Navi"],
            "resposta_correta": 'B'
        },
        {
            "pergunta": "Qual empresa criou o jogo Super Mario?",
            "opcoes": ["A) Sega", "B) Sony", "C) Microsoft", "D) Capcom", "E) Nintendo"],
            "resposta_correta": 'E'
        },
        {
            "pergunta": "Qual é o principal objetivo no jogo Among Us para os impostores?",
            "opcoes": ["A) Completar todas as tarefas", "B) Eliminar os tripulantes sem ser descoberto", 
                       "C) Ajudar os tripulantes", "D) Consertar as naves", "E) Coletar itens especiais"],
            "resposta_correta": 'B'
        },
        {
            "pergunta": "Qual desses jogos é um battle royale?",
            "opcoes": ["A) FIFA", "B) Call of Duty: Warzone", "C) The Witcher 3", 
                       "D) Assassin's Creed", "E) God of War"],
            "resposta_correta": 'B'
        }
    ]

    # Iterar sobre cada pergunta
    for i, pergunta in enumerate(perguntas, start=1):
        total_perguntas += 1  # Contar o total de perguntas
        print(f"{i}- {pergunta['pergunta']}")
        for opcao in pergunta['opcoes']:
            print(opcao)
        
        resposta_usuario = input("Digite a resposta correta: ").upper()
        score = VerificarRespostas(pergunta['resposta_correta'], resposta_usuario, score)
        print(f"Seu score atual é: {score}")

    # Resumo final
    print(f"\nVocê acertou {score} de {total_perguntas} perguntas.")
    print(f"Você errou {total_perguntas - score} perguntas.")

else:
    print("Saindo do QUIZ...")
