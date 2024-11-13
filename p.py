# Inicializa o colorama
from colorama import Fore, init
init(autoreset=True)

# Universal
from universal import *

# Quebra linhas
quebra_linha = Fore.WHITE + "." * 80  # Usar em divisões de funções
quebra_linha_ii = Fore.WHITE + "=" * 80  # Usar para o início e final do programa

# Defina a variável `end`
end = False

# Mensagem de início
print(quebra_linha_ii)
print(Fore.BLUE + 
            """
            Bem-vindo (a) ao Quizz
            Versão Beta
            """)

print(quebra_linha)

# Loop pricipal
def menu_principal():
    global end, quebra_linha, quebra_linha
    while not end:

        try:    # Avalia a entrada do usuário
            escolha_uma_dificuldade = int(input(Fore.BLUE + 
            """
            Escolha uma entrada:
            1 - Nível 1 (Bebezinho - 1 a 10)
            2 - Nível 2 (Normalzinho - 1 a 50)
            3 - Nível 3 (Cê é doido, doido?! - 1 a 100)
            4 - Nível 4 (Eu sabo muito - 1 a 1.000)
            0 - Sair
            """ +
            Fore.YELLOW + "Escolha uma entrada: "))
            print("")   # Espaço em branco
            print(quebra_linha)
            if escolha_uma_dificuldade == 0:
                end = True
                print(Fore.GREEN + """
            Saindo do Quizz. Até a próxima!
            Desenvolvido pela AnuTech - Dev. Luis Eduardo de Jesus Pires
            """ +
            Fore.MAGENTA + "Programa encerrado...\n")
                print(quebra_linha_ii)
                input()

            elif escolha_uma_dificuldade == 1:
                nivel_um()

            elif escolha_uma_dificuldade == 2:
                nivel_dois()

            elif escolha_uma_dificuldade == 3:
                nivel_tres()

            elif escolha_uma_dificuldade == 4:
                nivel_quatro()
                
            else:
                print(Fore.RED +
            """
            Entrada inválida
            """)
                print(quebra_linha)
        except ValueError:  # Exibe uma mensagem de erro
            print("")   # Linha em branco
            print(quebra_linha)
            print(Fore.RED +
            """
            Por favor, insira um número
            """)
            print(quebra_linha)

# Executar o menu principal
menu_principal()