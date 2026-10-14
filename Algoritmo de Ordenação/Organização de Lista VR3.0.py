#Sistema de Organização de Lista
#Notas de Alunos
#Feito por Lucas Verissimo
#Versão 1.0

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

notas = []
login = {
    "gioliano" : "bertoni",
    "alan" : "volei",
    "josilea" : "DOS"
}

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def main():
    tentativas = 3
    resposta_sim = ["sim", "s", "si"]
    resposta_nao = ["nao", "n", "na", "não", "nã"]
    print("=" * 50)
    print("Sistema de Organização de Lista")
    print("=" * 50)
    time.sleep(1.5)
    limpar_tela()

    print("\nLogin | Instrutor(a)/Docente/Professor(a)\n")
    print("Bom te Ver!")
    
    while tentativas > 0:
        print("Digite Seu Usuário")
        resposta_usuario = input(">  ").lower()
        print("Digite Sua Senha")
        resposta_senha = input(">  ")
        for usuario, senha in login:
            if resposta_usuario == usuario and resposta_senha == senha:
                print(f"Seja Bem-Vindo {resposta_usuario} Vamos organizar a sua lista de notas?")
                print("Insira o nome do aluno")
                aluno = input(">  ").strip().lower()
                limpar_tela()
                print(f"Quantas notas o aluno {aluno} teve?")
                quantidade_notas = int(input(">  ").strip())
                for i in range(1, quantidade_notas + 1):
                    print(f"Digite a {i}º nota")
                    nota = float(input(">  "))
                    notas.append(nota)
                print("Vamos Organizar a lista de Suas notas?")
                resposta_organizar = input(">  ")
                if resposta_organizar == resposta_sim:
                    print("Carregando...")
                    time.sleep(2.0)
                    resposta = bubble_sort(notas)
                    print(f"A Lista Organiza ficou assim {resposta}")
                elif resposta_organizar == resposta_nao:
                    print("Sua lista de notas foi:", notas)
                    print("Aperte Enter para Voltar ao Inicio do Sistema")
                    input(">  ")
                    main()
            else:
                tentativas -= 1
                print(f"Usuário ou Senha Incorretos, Aperte Enter para tentar novamente, tentativas restantes: {tentativas}")
                continue
main()