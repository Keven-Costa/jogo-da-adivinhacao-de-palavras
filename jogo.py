import random

palavras = ["ALGORITMO", "VARIÁVEL", "CONDICIONAL", "ITERAÇÃO", "FUNÇÃO", "ARRAY", "FRONTEND",
            "COMPILAÇÃO", "INTERFACE", "OBJETO", "HERANÇA", "POLIMORFISMO", "DESENVOLVEDOR",
            "LOOP", "BIBLIOTECA", "SINTAXE", "CLASSE", "MÉTODO", "COMPILADOR", "BACKEND"]
dicas = {"ALGORITMO": "Sequência de passos para resolver um problema.",
         "VARIÁVEL": "Armazena dados ou valores em um programa.",
         "CONDICIONAL": "Permite ao programa tomar decisões com base em condições",
         "ITERAÇÃO": " Repetição de um bloco de código até que uma condição seja atendida.",
         "FUNÇÃO": "Bloco de código que pode ser chamado e reutilizado.",
         "ARRAY": "Estrutura de dados que armazena elementos do mesmo tipo.",
         "FRONTEND": "Parte visível de um aplicativo ou site com a qual os usuários interagem.",
         "COMPILAÇÃO": "Processo de transformar código-fonte em código executável.",
         "INTERFACE": "Ponte de comunicação entre diferentes componentes de um sistema.",
         "OBJETO": "Instância de uma classe em programação orientada a objetos.",
         "HERANÇA": "Permite que uma classe herde atributos e métodos de outra.",
         "POLIMORFISMO": "Capacidade de objetos de diferentes classes responderem a métodos de maneira ",
         "DESENVOLVEDOR": "Pessoa que escreve, mantém e aprimora software.",
         "LOOP": "Estrutura que permite a repetição de código até que uma condição seja atendida.",
         "BIBLIOTECA": "Conjunto de funções e módulos pré-escritos para facilitar o desenvolvimento.",
         "SINTAXE": "Conjunto de regras que governam a estrutura e a escrita correta do código.",
         "CLASSE": "Modelo ou blueprint para criar objetos em programação orientada a objetos.",
         "MÉTODO": "Função associada a um objeto ou classe.",
         "COMPILADOR": " Software que traduz código-fonte em código de máquina.",
         "BACKEND": " Parte do sistema que lida com lógica e processamento de dados."
         }
i = 0
vidas = 0
palavra_oculta = random.choice(palavras)
auxiliar = ""

print("----------------------------------------")
print("    BEM-VINDO AO JOGO DA ADIVINHAÇÃO    ")
print("----------------------------------------")

dica = dicas[palavra_oculta]
print("Dica: {}".format(dica))

# print(palavra_oculta)
while True:
    letra = str(input("Digite uma LETRA: "))
    if letra == palavra_oculta[i]:
        print("Acertou")

        auxiliar = auxiliar + letra

        i = i + 1
        if auxiliar == palavra_oculta:
            print("PARABENS VC GANHOU!!!")

            break
    else:
        print("vc errou")
        i = i + 1
        auxiliar = auxiliar + palavra_oculta[i]
        vidas = vidas + 1
        if vidas == 5:
            print("GAME OVER!!!")
            break
