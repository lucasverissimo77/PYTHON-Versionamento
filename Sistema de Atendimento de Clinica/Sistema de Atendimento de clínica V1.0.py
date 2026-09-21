#Sistema de atendimento de uma clínica
#Feito por Lucas Verissimo
#Versão 1.0

import os
import time
import random

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

pacientes = []
senha_prioridade = ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", 
                    "P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", 
                    "P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030", 
                    "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", 
                    "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", 
                    "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", 
                    "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", 
                    "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080", 
                    "P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089", "P090", 
                    "P091", "P092", "P093", "P094", "P095", "P096", "P097", "P098", "P099", "P100"]

senha_normal = ["N100", "N101", "N102", "N103", "N104", "N105", "N106", "N107", "N108", "N109", 
                "N110", "N111", "N112", "N113", "N114", "N115", "N116", "N117", "N118", "N119", 
                "N120", "N121", "N122", "N123", "N124", "N125", "N126", "N127", "N128", "N129", 
                "N130", "N131", "N132", "N133", "N134", "N135", "N136", "N137", "N138", "N139", 
                "N140", "N141", "N142", "N143", "N144", "N145", "N146", "N147", "N148", "N149", 
                "N150", "N151", "N152", "N153", "N154", "N155", "N156", "N157", "N158", "N159", 
                "N160", "N161", "N162", "N163", "N164", "N165", "N166", "N167", "N168", "N169", 
                "N170", "N171", "N172", "N173", "N174", "N175", "N176", "N177", "N178", "N179", 
                "N180", "N181", "N182", "N183", "N184", "N185", "N186", "N187", "N188", "N189", 
                "N190", "N191", "N192", "N193", "N194", "N195", "N196", "N197", "N198", "N199"]

def principal():
    limpar_tela()
    print("---> Sistema de Pacientes <---\n")
    print("Opção 1: Marcar Consulta")
    print("Opção 2: Nossos Especialistas")
    print("Opção 3: Fila de Atendimento")
    print("Opção 4: Cancelar Consulta")
    print("Opção 0: Sair")
    print("Olá o senhor(a) {nome} Precisa escolher uma Opção (0-4):")
    resposta_opcoes = int(input(">  "))
    while resposta_opcoes != 0:
        if resposta_opcoes == 1:
            print("Consulta Marcada")
        if resposta_opcoes == 2:
            print("Nossos Especialistas")
        if resposta_opcoes == 3:
            print("Fila de Atendimento")
        if resposta_opcoes == 4:
            print("Cancelar Consulta")

def logar():
    global nome; global idade; global segundo_nome; global senha_escolhida
    limpar_tela()
    print("---Sistema de Login---\n")
    print("Para Fazer login precisamos do Seu nome/segundo nome/senha/idade (A senha é dada quando você se cadastra)\n")
    print("Digite seu nome")
    resposta_nome = input(">  ")
    print("Digite seu Segundo nome")
    resposta_segundo_nome = input(">  ")
    print("Digite sua idade")
    resposta_idade = int(input(">  "))
    print("Digite a senha dada quando você se cadastrou")
    resposta_senha = input(">  ")
    print("\nVerificando...")
    time.sleep(2)
    if resposta_nome == nome and resposta_idade == idade and resposta_segundo_nome == segundo_nome and resposta_senha == senha_escolhida:
        print("Redirecionando você para nosso sistema de Pacientes")
        time.sleep(2.5)
        principal()

def cadastrar():
    global nome; global idade; global segundo_nome; global senha_escolhida
    limpar_tela()
    print("---Sistema de Cadastro---")
    print("Digite Seu nome: ")
    nome = input(">  ")
    print("Digite seu Segundo nome: ")
    segundo_nome = input(">  ")
    print("Digite sua idade: ")
    try:
        idade = int(input(">  "))
        print("Seus Dados estão corretos ?")
        print(f"--> Nome Completo: {nome + " " + segundo_nome}")
        print(f"--> Idade: {idade}")
        resposta_cadastro = input(">  ").strip().lower()
        if resposta_cadastro == "sim" or resposta_cadastro == "s":
            if idade > 60 or idade < 15:
                senha_escolhida = random.choice(senha_prioridade)
            else:
                senha_escolhida = random.choice(senha_normal)
            print(f"Sua senha é {senha_escolhida} guarde ela para logar quando precisar.")
            print("Redirecionando para nosso sistema de Pacientes...")
            time.sleep(3.5)
            principal()
        elif resposta_cadastro == "nao" or resposta_cadastro == "n":
            print("Resetando")
            time.sleep(2.5)
            cadastrar()
        else:
            print("A sua resposta é inválida")
    except ValueError:
        print("Digite apenas caracteres válidos!")
        print("voltando...")
        time.sleep(3.0)
        limpar_tela()
        cadastrar()

def main():
    global nome; global idade; global segundo_nome; global senha_escolhida
    limpar_tela
    print("\n=======================")
    print("     Clínica Vida+   ")
    print("=======================\n")
    print("Olá seja bem vindo ao nosso Sistema da Clínica Vida+")
    print("O Senhor(a) possui cadastro em nosso sistema? ")
    resposta_inicial = input(">  ").strip().lower()
    if resposta_inicial == "sim" or resposta_inicial == "s":
        print("Seja bem vindo")
    elif resposta_inicial == "nao" or resposta_inicial == "n":
        print("Faça seu cadastro pelo nosso Sistema!")
        print("Redirecionando...")
        time.sleep(2.5)
        cadastrar()
    else:
        print("A sua resposta é inválida")
main()