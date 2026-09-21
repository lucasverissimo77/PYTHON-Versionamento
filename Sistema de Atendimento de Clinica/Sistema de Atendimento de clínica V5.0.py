#Sistema de atendimento de uma clínica
#Feito pelo "Grupo CTRL Z na vida real"/Lucas Verissimo, Kelvens Alves, Bryan Lessa
#Versão 5.0

import json
import os
import time
import random
from datetime import date, datetime



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()

data_atual = date(2026, 10, 1)

fila_normal  = 0
fila_prioridade = 0
fila_emergencia = 0

pacientes = []
medicos = {
    "Bernado" : {
    "Especialidade" : "Pediatra",
    "dias" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    "horarios" : ["8:00", "9:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "agenda": {}
    },
    "João" : {
    "Especialidade" : "Ortopedista",
    "dias" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    "horarios" : ["8:00", "9:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "agenda": {}
    },
    "Samara" : {
    "Especialidade" : "Ginecologista",
    "dias" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    "horarios" : ["8:00", "9:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "agenda": {}
    },
    "Agatha" : {
    "Especialidade" : "Cardiologista",
    "dias" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    "horarios" : ["8:00", "9:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "agenda": {}
    },
    "Pietra" : {
    "Especialidade" : "Clínico Geral",
    "dias" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    "horarios" : ["8:00", "9:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
    "agenda": {}
    }
}
qntd_medicos = 5;

def dias():
    print("---> Dias Disponiveis")
    


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

def remarcar_consulta():
    print("\n=====================")
    print("-->Remarcar Consulta<--")
    print("=====================")
    print(f"Olá {nome_completo} qual o nome do médico que iria te atender? (Bernado, Samara, João...)")
    nome_medico = input(">  ")
    if nome_medico not in medicos:
        print("Médico não encontrado!")
        time.sleep(2)
        return
    
    try:
        print("\n-- Consulta ANTIGA --")
        dia_antigo = int(input("Dia Antigo: \n>  "))
        horario_antigo = input("Horário antigo (ex: 9:30): \n>  ")
        chave_antiga = (dia_antigo, horario_antigo)
    except ValueError:
        print("A sua resposta é inválida, Tente Novamente...")
        print("Redirecionando você de volta ao inicio...")
        time.sleep(2.5)
        remarcar_consulta()
        
def marcar_consulta():
    limpar_tela()
    print("\n=====================")
    print("-->Marcar Consulta<--")
    print("=====================")
    print(f"Olá {nome_completo} primeiramente precisamos saber qual a situação de risco do(a) senhor(a)")
    print("\nOpção 1: Sem risco")
    print("Opção 2: Prioridade")
    print("Opção 3: Emergência")
    print("Opção 0: Sair")
    try:
        resposta_marcar_consulta = int(input(">  "))
        if resposta_marcar_consulta == 0:
            return
        print(f"\nMédicos Disponiveis: {list(medicos.keys())}")
        nome_medico = input("Digite o nome do médico: \n>  ")

        if nome_medico not in medicos:
            print("Médico não encontrado!")
            time.sleep(2)
            marcar_consulta()
            return
        print(f"Dias disponíveis: {medicos[nome_medico]['dias'][:15]}...")
        dia = input("Escolha o dia: \n>  ")
        print(f"Horários disponíveis: {medicos[nome_medico]['horarios']}")
        horario = input("Escolha o horário (ex: 8:00): \n>  ")

        chave = (dia, horario)
        if chave in medicos[nome_medico]["agenda"]:
            print(f"Erro: Esse horário já está ocupado por {medicos[nome_medico]['agenda'][chave]}")
            time.sleep(3)
            marcar_consulta()
            return
        
        if resposta_marcar_consulta == 1:
            fila_normal.append(nome_completo)
            medicos[nome_medico]["agenda"][chave] = nome_completo
            print(f"Consulta marcada sem risco com {nome_medico} dia {dia} às {horario}")
            
        elif resposta_marcar_consulta == 2:
            fila_prioridade.append(nome_completo)
            medicos[nome_medico]["agenda"][chave] = nome_completo
            print(f"Consulta marcada prioridade com {nome_medico} dia {dia} às {horario}")
            
        elif resposta_marcar_consulta == 3:
            fila_emergencia.append(nome_completo)
            medicos[nome_medico]["agenda"][chave] = nome_completo
            print(f"Consulta marcada Emergência com {nome_medico} dia {dia} às {horario}")
        print("Aperte Enter para sair: ")
        input(">  ")
            
    except ValueError:
        print("O valor Inserido não é válido")
        print("Redirecionando de volta ao início...")
        time.sleep(2.5)
        marcar_consulta()
    
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
            print("Carregando...")
            time.sleep(2.5)
            marcar_consulta()
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
    global nome; global idade; global segundo_nome; global cpf; global medico; global especialidade
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
    if resposta_nome_completo == nome_completo and resposta_idade == idade and resposta_senha == cpf:
        print("Redirecionando você para nosso sistema de Pacientes")
        time.sleep(2.5)
        principal()

def cadastrar():
    global idade; global cpf; global nome_completo; global nome; global segundo_nome; global medico; global especialidade
    limpar_tela()
    print("---Sistema de Cadastro---")
    print("Digite Seu nome: ")
    nome = input(">  ")
    print("Digite seu Segundo nome: ")
    print("Digite Seu CPF, ele será usado como senha:")
    cpf = int(input(">  "))
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
            print(f"Sua senha é {cpf} guarde ela para logar quando precisar.")
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
    global idade; global cpf; global nome_completo; global medico; global especialidade; 
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



