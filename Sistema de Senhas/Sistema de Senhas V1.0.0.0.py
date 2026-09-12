#Sistema de Senhas
#Feito por Lucas Verissimo
#Versão 1.0.0.0


import random
import os
import time


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)


idade = 0
senha_prioridade = ["N001", "N002", "N003", "N004", "N005", "N006", "N007", "N008", "N009", "N010"]
senha_normal = ["S001", "S002", "S003", "S004", "S005","S006", "S007", "S008", "S009", "S010"]

def menor_idade():
    limpar_tela()
    print("\n=== ===Atendimento Prioritário Pediatrico=== ===\n")
    senha_escolhida = random.choice(senha_prioridade)
    print(f"Sua senha é de nível prioridade\nSenha: {senha_escolhida}")
    print("\nDigite Enter para voltar ao menu inicial")
    input(">  ")

def idade_normal():
    print("\n--- ---Atendimento Sem Risco--- ---\n")
    senha_escolhida = random.choice(senha_normal)
    print(f"Sua senha é de nível prioridade\nSenha: {senha_escolhida}")
    print("\nDigite Enter para voltar ao menu inicial")
    input(">  ")

def idoso_idade():
    print("\n=== ===Atendimento Prioritário Para +60=== ===\n")
    senha_escolhida = random.choice(senha_prioridade)
    print(f"Sua senha é de nível prioridade\nSenha: {senha_escolhida}")
    print("\nDigite Enter para voltar ao menu inicial")
    input(">  ")

def inicio(idade):
    while idade >= 0:
        try:
            limpar_tela()
            print("\n--- SUS Kelvems ---\n")
            print("Aqui em nossa Instituição De Saúde, Daremos a senha de acordo com a idade da pessoa!!")
            print("Qual sua Idade?")
            idade = int(input(">  "))
            if idade <= 15:
                limpar_tela()
                menor_idade()
            if 15 <= idade <=60:
                limpar_tela()
                idade_normal()
            if idade >= 60:
                limpar_tela()
                idoso_idade()
        except ValueError:
            print("Error 303\nDigite Somente Números")
            print("Voltando ao Menu...")
            time.sleep(3)
inicio(idade)


        