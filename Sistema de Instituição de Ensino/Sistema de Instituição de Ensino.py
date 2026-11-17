#Sistema de Instituição de Ensino em Python
#Feito por Lucas Verissimo Fundador do KODEFORGE | https://www.kodeforge.com.br
#Versão 1.0

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()

lista_alunos = ["kelvens", "joao", "lucas"]

def procurar_aluno():
    print("=== Procuradoria de Alunos ===")
    print("Digite o nome do aluno que você deseja achar")
    aluno = input(">  ").strip()
    if aluno in lista_alunos:
        print("Aluno encontrado")
        print("Digite Enter para voltar ao menu principal")
        input(">  ")
        main()
    else:
        print("Aluno nao encontrado")
        print("Digite Enter para tentar novamente")
        input(">  ")
        procurar_aluno()

def excluir_aluno():
    print("=== Exclusão de Registro ===")
    print("Digite o nome do aluno que você deseja excluir")
    resposta = input(">  ").strip()
    if resposta in lista_alunos:
        lista_alunos.remove(resposta)
        print("Digite Enter para voltar ao menu inicial")
        input(">  ")
        main()
    else:
        print("Aluno não encontrado tente novamente")
        print("Digite Enter para tentar novamente:")
        input(">  ")
        excluir_aluno()

def listar_alunos():
    print("=== Listagem de Alunos ===\n")
    for i, aluno in enumerate(lista_alunos, start=1):
        print(f"Nome: {aluno}\nNº DE REGISTRO: {i}")
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
        lista_alunos.append(aluno)
    print("Aperte Enter para ir no menu")
    input(">  ")
    main()


def main():
    print("\n=== Instituição KodeForge ===\n")
    print("==> Opções")
    print("Opção 1: Cadastrar aluno")
    print("Opção 2: Listar Alunos")
    print("Opção 3: Procurar Aluno")
    print("Opção 4: Excluir aluno")
    print("Opção 5: sair\n")
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
        procurar_aluno()
    elif resposta_usuario == 4:
        print("Carregando Opção 4...")
        time.sleep(2.5)
        limpar_tela()
        excluir_aluno()
    elif resposta_usuario == 5:
        print("Encerrando sistema...")
        limpar_tela()
    else:
        print("Opção inválida aperte enter para tentar novamente")
        input(">  ")
        main()
main()