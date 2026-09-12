#Sistema de Folha de Pagamento
#Versão 3.0.0.0
#Feito Por Lucas Verissimo

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(1)

funcionario = 0
salario_bruto = 0
salario_final = 0
horas_extras = 0
tentativas = 3


def administrador():
        salarios = []
        horas = []
        nome_funcionario = []
        try:
            limpar_tela()
            print("\n---Seja Bem-Vindo grandioso Adm---\n")
            print(f"A empresa aonde o senhor {resposta_usuario} está logado é a empresa da {empresa}")
            print("digite quantos funcionarios sua empresa tem: ")
            qntd_funcionario = int(input(">  "))
            for i in range(1, qntd_funcionario +1):
                print(f"Digite o nome do {i}º funcionario")
                nome = input(">  ")
                nome_funcionario.append(nome)
            limpar_tela()
            for i, nome in enumerate(nome_funcionario, start=1):
                print(f"{i}º Nome: {nome}\n")
                print(f"Digite o salário Bruto do funcionario {nome}: ")
                salario_bruto = float(input(">  "))
                print(f"O funcionario {nome} Fez horas extras ? (Sim/Não)")
                resposta_adm = input(">  ")
                if resposta_adm == "Sim" or resposta_adm == "sim" or resposta_adm == "s":
                    print(f"Informe quantas horas extras o funcionario {nome} trabalhou a mais em sua empresa: ")
                    horas_extras = float(input(">  "))
                    salario_final = salario_bruto + (horas_extras * 25)
                elif resposta_adm == "Nao" or resposta_adm == "nao" or resposta_adm == "n":
                    horas_extras = 0
                    salario_final = salario_bruto
                    print("\nCarregando...\n")
                    time.sleep(5)
                salarios.append(salario_final)
                horas.append(horas_extras)
            limpar_tela()
            print("\n=== ===Sistema de Funcionarios=== ===\n")
            for i in range(qntd_funcionario):
                print(f"{i+1}º Nome: {nome_funcionario[i]}")
                print(f"Salário Final: {salarios[i]}")
                print(f"Horas Extras: {horas[i]}\n")
                input("Aperte Enter para Encerrar o Sistema")
                break
                
        except ValueError:
            print("Digite apenas os caracteres válidos nas Opções! ")

def empresa_dell():
    global resposta_usuario
    global tentativas
    limpar_tela()
    while tentativas > 0:
        usuario_dell = "dell_adm"
        senha_dell = "123adm"
        print("Digite o nome de usuário Adm da Empresa Dell: ")
        resposta_usuario = input(">  ").strip().lower()
        print("Digite a senha de usuário Adm da Empresa Dell: ")
        resposta_senha = input(">  ")
        if resposta_usuario == usuario_dell and resposta_senha == senha_dell:
            print("Carregando...")
            administrador()
        else:
            tentativas -= 1
            print(f"Você Errou o usuário ou a senha você tem mais {tentativas} tentativas")
            continue
    if tentativas == 0:
        print("Acesso bloqueado")

def empresa_valle():
    global resposta_usuario
    global tentativas
    limpar_tela()
    while tentativas > 0:
        usuario_valle = "valle_adm"
        senha_valle = "123adm"
        print("Digite o nome de usuário Adm da Empresa Valle")
        resposta_usuario = input(">  ").strip().lower()
        print("Digite a senha de usuário Adm da Empresa Valle")
        resposta_senha = input(">  ")
        if resposta_usuario == usuario_valle and resposta_senha == senha_valle:
            administrador()
        else:
            tentativas -= 1
            print(f"Você Errou o usuário ou a senha você tem mais {tentativas} tentativas")
            continue
    if tentativas == 0:
        print("Acesso Bloqueado!")

def empresa_amazon():
    global resposta_usuario
    global tentativas
    limpar_tela()
    while tentativas > 0:
        usuario_amazon = "amazon_adm"
        senha_amazon = "123adm"
        print("Digite o nome de usuário Adm da Empresa Amazon")
        resposta_usuario = input(">  ").strip().lower()
        print("Digite a senha de usuário Adm da Empresa Amazon")
        resposta_senha = input(">  ")
        if resposta_usuario == usuario_amazon and resposta_senha == senha_amazon:
            administrador()
        else:
            tentativas -= 1
            print(f"Você Errou o usuário ou a senha você tem mais {tentativas} tentativas")
            continue
    if tentativas == 0:
        print("Acesso Bloqueado!")

def empresa_dolly():
    global resposta_usuario
    global tentativas
    limpar_tela()
    while tentativas > 0:
        usuario_dolly = "dolly_adm"
        senha_dolly = "123adm"
        print("Digite o nome de usuário Adm da Empresa Dolly")
        resposta_usuario = input(">  ").strip().lower()
        print("Digite a senha de usuário Adm da Empresa Dolly")
        resposta_senha = input(">  ")
        if resposta_usuario == usuario_dolly and resposta_senha == senha_dolly:
            administrador()
        else:
            tentativas -= 1
            print(f"Você Errou o usuário ou a senha você tem mais {tentativas} tentativas")
            continue
    if tentativas == 0:
        print("Acesso Bloqueado!")



def main():
    global empresa
    limpar_tela()
    while True:
        try:
            print("\n=-= =-=Sistema de Empresas=-= =-=\n")
            print("1 - Empresa da Dell")
            print("2 - Empresa da Valle")
            print("3 - Empresa da Amazon")
            print("4 - Empresa da Dolly")
            print("0 - Sair\n")
            print("Digite o Número da Empresa de onde você é administrador: ")
            opcao = int(input(">  "))
            if opcao == 1:
                empresa = "Dell"
                limpar_tela()
                empresa_dell()
            elif opcao == 2:
                empresa = "Valle"
                limpar_tela()
                empresa_valle()
            elif opcao == 3:
                empresa = "Amazon"
                limpar_tela()
                empresa_amazon()
            elif opcao == 4:
                empresa = "Dolly"
                limpar_tela()
                empresa_dolly()
            elif opcao == 0:
                limpar_tela()
                print("Saindo do Sistema...")
                print("Aperte Enter para confirmar a saída: ")
                input(">  ").strip().lower()
                limpar_tela()
                break
            else:
                print("Digite apenas números!!")
        except ValueError:
            print("Digite apenas caracteres válidos")
main()
