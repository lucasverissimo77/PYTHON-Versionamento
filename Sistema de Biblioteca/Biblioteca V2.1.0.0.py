# Sistema de biblioteca, desenvolvido por Yuri Quites, Lucas Veríssimo e Caio Mota
# V2.1.0.0 (Corrigido)

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)
 
livros = 50
livros_emprestados = 0
max_livros = 50


def emprestar_livro():
    global livros, livros_emprestados
    limpar_tela()
    print("=== EMPRÉSTIMO DE LIVROS ===")

    if livros == 0:
        print("\nDesculpe, todos os livros estão emprestados no momento!")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    while True:
        try:
            quantidade = int(input(f"Quantos livros você desejar alugar, temos esta quantidade de livros disponiveis {livros} (use apenas números)?: "))
            
            if quantidade <=0:
                print("Por favor digite um número maior que zero. \n")
                continue

            if quantidade <= livros:
                livros -= quantidade
                livros_emprestados += quantidade
                print(f"Parábens! Você alugou {quantidade} livro(s).")
                input("\nPressione Enter para voltar ao Menu")
                return
            else:
                print(f"\nVocê está tentando pegar uma quantia indisponível de livros. Temos apenas {livros} em estoque")
                return
        except ValueError:
            print("\nErro: Utilize apenas números inteiros seu animal.\n")
    

def devolucao_livros():
    global livros, livros_emprestados
    limpar_tela()
    print("=== Devolução de Livros ===")

    if livros_emprestados == 0:
        print("\nTodos os livros já estão na biblioteca. Não há nada para devolver!")
        input("\nDigite Enter para voltar ao menu seu boçal!!")
        return 
    while True:
        try:
            print(f"Livros atualmente emprestados (===fora da biblioteca===): {livros_emprestados}")
            devolucao = int(input("Quantos livros você desejar devolver (use apenas números)?: "))
            if devolucao <= 0:
                print("Por favor, digite uma quantidade maior que zero(0)")
                continue
            if devolucao <= livros_emprestados:
                livros += devolucao
                livros_emprestados -= devolucao
                print(f"\nParabéns! Você devolveu {devolucao} livro(s).")
                input("Digite Enter para voltar ao menu...")
                return
            else:
                print(f"\nQuantidade inválida!! Você só pode devolver até {livros_emprestados} livro(s).\n")
        except ValueError:
            print("\nUtilize apenas números inteiros!!!\n")

    


def quantidade_livros():
    limpar_tela()
    print("=== Status de Estoque ===")
    print(f"Livros disponiveis em nosso estoque: {livros}")
    print(f"Livros emprestados (Em algum lugar muito distante daqui.): {livros_emprestados}")
    print(f"Capacidade total do sistema: {max_livros}")
    input("\nPressione Enter para voltar ao menu...")
    

def sair():     
    print("Ok, você quer sair de nossa biblioteca. Então Adeus, boçal.")





while True:
    limpar_tela()
    print("==================================================")
    print("     Sistema de Biblioteca - Yuri, Lucas e Caio ")
    print("==================================================")
    print(" [1] Emprestar Livro(s)")
    print(" [2] Devolver Livro(s)")
    print(" [3] Verificar Estoque / Quantidade")
    print(" [4] Sair do Sistema")
    print("===================================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        emprestar_livro()
    elif opcao == "2":
        devolucao_livros()
    elif opcao == "3":
        quantidade_livros()
    elif opcao == "4":
        limpar_tela()
        print("Finalizando o sistema vagabundo, Até logo!")
        time.sleep(1)
        break
    else:
        print("\nOpção Inválida! Escolha um número de 1 a 4.")
        time.sleep(1.5)
    






