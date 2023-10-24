import random

palavras = ["algoritmo", "variável", "condicional", "iteração", "função", "array", "frontend",
            "compilação", "interface", "objeto", "herança", "polimorfismo", "desenvolvedor",
            "loop", "biblioteca", "sintaxe", "classe", "método", "compilador", "backend"]
letras_digitadas = []
dicas = {"algoritmo": "sequência de passos para resolver um problema.",
         "variável": "armazena dados ou valores em um programa.",
         "condicional": "permite ao programa tomar decisões com base em condições",
         "iteração": "repetição de um bloco de código até que uma condição seja atendida.",
         "função": "bloco de código que pode ser chamado e reutilizado.",
         "array": "estrutura de dados que armazena elementos do mesmo tipo.",
         "frontend": "parte visível de um aplicativo ou site com a qual os usuários interagem.",
         "compilação": "processo de transformar código-fonte em código executável.",
         "interface": "ponte de comunicação entre diferentes componentes de um sistema.",
         "objeto": "instância de uma classe em programação orientada a objetos.",
         "herança": "permite que uma classe herde atributos e métodos de outra.",
         "polimorfismo": "capacidade de objetos de diferentes classes responderem a métodos de maneira polimórfica",
         "desenvolvedor": "pessoa que escreve, mantém e aprimora software.",
         "loop": "estrutura que permite a repetição de código até que uma condição seja atendida.",
         "biblioteca": "conjunto de funções e módulos pré-escritos para facilitar o desenvolvimento.",
         "sintaxe": "conjunto de regras que governam a estrutura e a escrita correta do código.",
         "classe": "modelo ou blueprint para criar objetos em programação orientada a objetos.",
         "método": "função associada a um objeto ou classe.",
         "compilador": "software que traduz código-fonte em código de máquina.",
         "backend": "parte do sistema que lida com lógica e processamento de dados."
         }
vidas = 5
letra = None
palavra_oculta = None
dica = None

palavra_oculta = random.choice(palavras)
def boasvindas():
    print("----------------------------------------")
    print("    BEM-VINDO AO JOGO DA ADIVINHAÇÃO    ")
    print("----------------------------------------")
def dica():
    dica = dicas[palavra_oculta]
    print("Dica: {}".format(dica))
def verifica_letra(letra):
    if letra in letras_digitadas:
        print(f"A letra '{letra}' já foi digitada.")
    elif letra in palavra_oculta:
        letras_digitadas.append(letra)
        print("ACERTOU!!!")
        return True
    else:
        letras_digitadas.append(letra)
        print("VOCÊ ERROU!!!")
        return False
def letras_adivinhadas():
    palavra_adivinhada = ""
    for letra in palavra_oculta:
        if letra in letras_digitadas:
            palavra_adivinhada += letra
        else:
            palavra_adivinhada += "_"
    return palavra_adivinhada

boasvindas()
dica()
while vidas > 0:
    letra = input("Digite uma LETRA: ").lower()
    if verifica_letra(letra):
        palavra_adivinhada = letras_adivinhadas()
        print(palavra_adivinhada)
        if palavra_adivinhada == palavra_oculta:
            print(f"Parabéns! Você adivinhou a palavra: {palavra_oculta}")
            break
    else:
        vidas -= 1
        print(f"Você tem {vidas} vidas restantes.")

if vidas == 0:
    print(f"Suas vidas acabaram. A palavra era: {palavra_oculta}")
