#Sistema de atendimento de uma clínica
#Feito pelo "Grupo CTRL Z na vida real"/Lucas Verissimo, Kelvens Alves, Bryan Lessa
#Versão 3.0

import os
import time
import random

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

pacientes = []
senha_prioridade = "P" + str(random.randint(1, 100))

senha_normal = "N" + str(random.randint(101, 201))

medicos = {
    "nome" : "especialidade",
    "Bernado" : "Pediatrico",
    "João" : "Dermatologista",
    "Samara" : "Ginecologista",
    "Agatha" : "Cardiologista",
    "Pietra" : "Psicóloga",
}
fila_normal  = 0
fila_prioridade = 0
fila_emergencia = 0

def fila_atendimento():
    limpar_tela()
    print("===> Fila De Atendimento <===\n")
    print("Opção 0: Sair: ")
    print("Opção 1: Fila de Atendimento Normal")
    print("Opção 2: Fila de Atendimento Prioridade")
    print("Opção 3: Fila de Atendimento Emergencia\n")
    print("Escolha uma Opção (0-4): ")
    try:
        resposta_fila = int(input(">  "))
        while resposta_fila != 0:
            if resposta_fila == 1:
                print(f"O atendimento da fila de sem risco é de {fila_normal} pessoas")
                print("Aperte Enter para sair: ")
                input(">  ")
            elif resposta_fila == 2:
                print(f"O atendimento da fila de Prioritária é de {fila_prioridade} pessoas")
                print("Aperte Enter para sair: ")
                input(">  ")
            elif resposta_fila == 3:
                print(f"o atendimento da fila de emergência é de {fila_emergencia} pessoas")
                print("Aperte Enter para sair: ")
                input(">  ") 
            else:
                print("Fila de atendimento não encontrada")
                print("Redirecionando você ao inicio...")
                time.sleep(2.5)
                fila_atendimento()
    except ValueError:
            print("O valor inserido não é válido!")
            print("Voltando ao inicio...")
            time.sleep(2.5)
            fila_atendimento()
            
    
    
def especialistas():
    global medico; global especialidade; 
    limpar_tela()
    print("===========================")
    print("---Nossos Especialistas---")
    print("============================")
    for medico, especialidade in medicos.items():
        print(f"Médico: {medico}        Especialidade: {especialidade}")
        print("---------------------------------------------------------")
    print("Aperte Enter para Voltar ao menu inicial")
    input(">  ")
    principal()

def principal():
    limpar_tela()
    print("---> Sistema de Pacientes <---\n")
    print("Opção 1: Marcar Consulta")
    print("Opção 2: Remarcar Consulta")
    print("Opção 3: Cancelar Consulta")
    print("Opção 4: Nossos Especialistas")
    print("Opção 5: Fila de Atendimento")
    print("Opção 0: Sair")
    print(f"Olá o senhor(a) {nome_completo} Precisa escolher uma Opção (0-5):")
    resposta_opcoes = int(input(">  "))
    while resposta_opcoes != 0:
        if resposta_opcoes == 1:
            print("Consulta Marcada")
        elif resposta_opcoes == 2:
            print("Consulta remarcada")
        elif resposta_opcoes == 3:
            print("Cancelar Consulta")
        elif resposta_opcoes == 4:
            print("Carregando...")
            time.sleep(2.5)
            especialistas()
        elif resposta_opcoes == 5:
            print("Carregando...")
            time.sleep(2.5)
            fila_atendimento()


def logar():
    global nome; global idade; global segundo_nome; global senha_escolhida; global medico; global especialidade
    limpar_tela()
    print("---Sistema de Login---\n")
    print("Para Fazer login precisamos do Seu nome/segundo nome/senha/idade (A senha é dada quando você se cadastra)\n")
    print("Digite seu primeiro e segundo nome")
    resposta_nome_completo = input(">  ")
    print("Digite sua idade")
    resposta_idade = int(input(">  "))
    print("Digite a senha dada quando você se cadastrou")
    resposta_senha = input(">  ")
    print("\nVerificando...")
    time.sleep(2)
    if resposta_nome_completo == nome_completo and resposta_idade == idade and resposta_senha == senha_escolhida:
        print("Redirecionando você para nosso sistema de Pacientes")
        time.sleep(2.5)
        principal()

def cadastrar():
    global idade; global senha_escolhida; global nome_completo; global nome; global segundo_nome; global medico; global especialidade
    limpar_tela()
    print("---Sistema de Cadastro---")
    print("Digite Seu nome: ")
    nome = input(">  ")
    print("Digite seu Segundo nome: ")
    segundo_nome = input(">  ")
    print("Digite sua idade: ")
    nome_completo = nome + " " + segundo_nome
    try:
        idade = int(input(">  "))
        print("Seus Dados estão corretos ?")
        print(f"--> Nome Completo: {nome_completo}")
        print(f"--> Idade: {idade}")
        resposta_cadastro = input(">  ").strip().lower()
        if resposta_cadastro == "sim" or resposta_cadastro == "s":
            if idade > 60 or idade < 15:
                senha_escolhida = senha_prioridade
            elif idade < 0:
                print("A idade Escolhida não é valida!")
            else:
                senha_escolhida = senha_normal
            print(f"Sua senha é {senha_escolhida} guarde ela para logar quando precisar.")
            print("Redirecionando para nosso sistema de Pacientes...")
            time.sleep(4.5)
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
    global idade; global senha_escolhida; global nome_completo; global medico; global especialidade; 
    limpar_tela()
    print("\n=======================")
    print("     Clínica Vida+   ")
    print("=======================\n")
    print("Olá seja bem vindo ao nosso Sistema da Clínica Vida+")
    print("O Senhor(a) possui cadastro em nosso sistema? ")
    resposta_inicial = input(">  ").strip().lower()
    if resposta_inicial == "sim" or resposta_inicial == "s":
        print("Faça seu Login em Nosso Sistema!")
        print("Redirecionando...")
        time.sleep(2.5)
        logar()
    elif resposta_inicial == "nao" or resposta_inicial == "n":
        print("Faça seu cadastro pelo nosso Sistema!")
        print("Redirecionando...")
        time.sleep(2.5)
        cadastrar()
    else:
        print("A sua resposta é inválida")
main()



