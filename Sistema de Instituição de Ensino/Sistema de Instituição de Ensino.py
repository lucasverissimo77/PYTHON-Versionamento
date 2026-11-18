#Sistema de Instituição de Ensino em Python
#Feito por Lucas Verissimo Fundador do KODEFORGE | https://www.kodeforge.com.br
#Versão 2.0

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()

lista_alunos = ["kelvens", "joao", "lucas", "Marcos", "Matheus", "Mateus"]

def selection_sort():
    print("=== Sistema de Ordenação Selection Sort ===")
    n = len(lista_alunos)

    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista_alunos[j] < lista_alunos[menor].lower():
                menor = j
        lista_alunos[i], lista_alunos[menor] = lista_alunos[menor], lista_alunos[i]
    print("Lista Ordenada com Sucesso")
    print(lista_alunos)
    print("Aperte Enter para voltar ao Menu")
    input(">  ")
    limpar_tela()
    main()


def bubble_sort():
    print("=== Sistema de Ordenação Bubble Sort ===")
    n = len(lista_alunos)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_alunos[j] > lista_alunos[j + 1].lower():
                lista_alunos[j], lista_alunos[j + 1] = lista_alunos[j+1], lista_alunos[j]
    print("Lista Ordenada Com sucesso")
    print(lista_alunos)
    print("Aperte Enter para voltar ao Menu")
    input(">  ")
    limpar_tela()
    main()

def ordernar_lista():
    print("=== Ordernação de Lista ===\n")
    print("Digite a opção desejada para a ordenação")
    print("Opção 1: Bubble sort")
    print("Opção 2: Selection sort")
    print("Opção 3: Sair")
    resposta = int(input(">  ").strip())
    if resposta == 1:
        print("Carregando Opção 1...")
        time.sleep(1.5)
        limpar_tela()
        bubble_sort()
    elif resposta == 2:
        print("Carregando Opção 2...")
        time.sleep(1.5)
        limpar_tela()


def busca_sequencial(aluno_procurado):
    alunos_encontrados = 0
    print("=== Busca Sequencial ===\n")
    encontrado = False
    for i, aluno in enumerate(lista_alunos, start=1):
        alunos_encontrados +=1
        if aluno == aluno_procurado:
            print(f"O aluno {aluno_procurado} foi achado com registro N: {i}")
            encontrado = True
            time.sleep(1)
    if not encontrado:
        print(f"O aluno não foi encontrado na lista")

    print(f"Alunos Encontrados na Operação {alunos_encontrados}")
    print("Digite Enter para voltar ao menu principal")
    time.sleep(2.5)
    limpar_tela()
    main()

def busca_binaria(aluno_procurado):
    print("=== Busca Binária ===\n")
    inicio = 0
    fim = len(lista_alunos) -1
    encontrado = False
    alunos_encontrados = len(lista_alunos)

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista_alunos[meio] == aluno_procurado:
            print(f"O aluno {aluno_procurado} foi encontrado com Número de Registro: {meio}")
            encontrado = True
        elif lista_alunos[meio] < aluno_procurado:
            inicio = meio + 1

        else:
            fim = meio - 1
    if not encontrado:
        print("O aluno não foi encontrado na lista")
        print("Digite Enter para voltar ao menu Principal")
        input(">  ")
        limpar_tela()
        main()

    print(f"Alunos totais encontrados na operação {alunos_encontrados}")
    print("Digite Enter para voltar ao Menu Principal")
    input(">  ")
    limpar_tela()
    main()
            

def busca_direta(aluno):
    print("=== Busca Direta ===\n")
    if aluno in lista_alunos:
        print(f"Aluno {aluno} encontrado")
        print("Digite Enter para voltar ao menu principal")
        input(">  ")
        main()
    else:
        print("Aluno não encontrado")
        print("Deseja tentar novamente?")
        print("Opção 1: Sim \nOpção 2: Não")
        try:
            resposta = int(input(">  ").strip())
        except ValueError:
            print("Valor inserido não é válido, tente novamente...")
            print("Aperte Enter para Tentar novamente")
            input(">  ")
            procurar_aluno()
        if resposta == 1:
            print("Tentando Novamente...")
            time.sleep(1.5)
            procurar_aluno()
        elif resposta == 2:
            print("Indo ao Menu Principal")
            time.sleep(1.5)
            main()

def procurar_aluno():
    print("=== Procuradoria de Alunos ===")
    print("Você deseja buscar o aluno com qual tipo de busca")
    print("Opção 1: Busca Binária (Recomendado se tiver muitos alunos)")
    print("Opção 2: Busca Sequencial")
    print("Opção 3: Busca Direta")
    try:
        resposta = int(input(">  ").strip())
    except ValueError:
        print("Valor inserido não é válido, tente novamente...")
        print("Aperte Enter para Tentar novamente")
        input(">  ")
        procurar_aluno()
    print("Digite o nome do aluno que você deseja achar")
    nome_aluno = input(">  ").strip().lower()
    if resposta == 1:
        print("Carregando Opção 1...")
        time.sleep(1.5)
        limpar_tela()
        busca_binaria(nome_aluno)
    elif resposta == 2:
        print("Carregando Opção 2...")
        time.sleep(1.5)
        limpar_tela()
        busca_sequencial(nome_aluno)
    elif resposta == 3:
        print("Carregando Opção 3...")
        time.sleep(1.5)
        limpar_tela()
        busca_direta()
    else:
        print("Opção digitada é inválida")
        print("Digite Enter para tentar novamente")
        input(">  ")
        limpar_tela()
        procurar_aluno()

def excluir_aluno():
    print("=== Exclusão de Registro ===")
    print("Digite o nome do aluno que você deseja excluir")
    resposta = input(">  ").strip().lower()
    if resposta in lista_alunos:
        lista_alunos.remove(resposta)
        print("Digite Enter para voltar ao menu inicial")
        input(">  ")
        main()
    else:
        print("Aluno não encontrado tente novamente")
        print("Digite Enter para tentar novamente:")
        input(">  ")
        limpar_tela()
        excluir_aluno()

def listar_alunos():
    print("=== Listagem de Alunos ===\n")
    for i, aluno in enumerate(lista_alunos, start=1):
        print(f"Nome: {aluno}\nNº DE REGISTRO: {i}")
    print(f"Alunos totais: {len(lista_alunos)}")
    print("Aperte Enter para voltar ao menu")
    input(">  ")
    main()

def cadastrar_aluno():
    print("=== Cadastro de alunos ===\n")
    print("quantos alunos o senhor deseja cadastrar")
    quantidade_alunos = int(input(">  "))
    for i in range(1, quantidade_alunos + 1):
        print(f"Digite o nome do {i}º aluno(a)")
        aluno = input(">  ")
        if aluno in lista_alunos:
            print("O aluno já está cadastrado, coloque um sobrenome se for outra pessoa.")
        else:
            print("Aluno Cadastrado Com Sucesso")
            lista_alunos.append(aluno)
    print("Aperte Enter para ir no menu")
    limpar_tela()
    input(">  ")
    main()


def main():
    print("\n=== Instituição KodeForge ===\n")
    print("==> Opções")
    print("Opção 1: Cadastrar aluno")
    print("Opção 2: Listar Alunos")
    print("Opção 3: Ordenar Lista de Alunos")
    print("Opção 4: Procurar Aluno")
    print("Opção 5: Excluir aluno")
    print("Opção 6: sair\n")
    print("Digite a opção que o senhor deseja escolher")
    try:
        resposta_usuario = int(input(">  "))
    except ValueError:
        print("O valor que você inseriu e invalido tente novamente...")
        print("Aperte Enter para voltar ao menu")
        input(">  ")
        main()
    if resposta_usuario == 1:
        print("Carregando Opção 1...")
        time.sleep(2.5)
        limpar_tela()
        cadastrar_aluno()
    elif resposta_usuario == 2:
        print("Carregando Opção 2...")
        time.sleep(2.5)
        limpar_tela()
        listar_alunos()
    elif resposta_usuario == 3:
        print("Carregando Opção 3...")
        time.sleep(2.5)
        limpar_tela()
        ordernar_lista()
    elif resposta_usuario == 4:
        print("Carregando Opção 4...")
        time.sleep(2.5)
        limpar_tela()
        procurar_aluno()
    elif resposta_usuario == 5:
        print("Carregando Opção 5...")
        time.sleep(2.5)
        limpar_tela()
        excluir_aluno()
    elif resposta_usuario == 6:
        print("Encerrando sistema...")
        limpar_tela()
    else:
        print("Opção inválida aperte enter para tentar novamente")
        input(">  ")
        main()
main()