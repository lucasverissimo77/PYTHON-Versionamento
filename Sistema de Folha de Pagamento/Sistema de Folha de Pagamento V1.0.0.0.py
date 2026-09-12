#Sistema de Folha de Pagamento
#Versão 1.0.0.0
#Feito Por Lucas Verissimo

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(1)

funcionario = 0
nome_funcionario = None
salario = 0
horas_extras = 0
tentativas = 3

def empresa_dell():
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
            print("Seja bem vindo!")
        else:
            tentativas -= 1
            print(f"Você Errou o usuário ou a senha você tem mais {tentativas} tentativas")
            continue
    if tentativas == 0:
        print("Acesso bloqueado")

def empresa_valle():
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
            print("Seja Bem-Vindo!")
        else:
            tentativas -= 1
            print(f"Você Errou o usuário ou a senha você tem mais {tentativas} tentativas")
            continue
    if tentativas == 0:
        print("Acesso Bloqueado!")

def empresa_amazon():
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
            print("Seja Bem-Vindo!")
        else:
            tentativas -= 1
            print(f"Você Errou o usuário ou a senha você tem mais {tentativas} tentativas")
            continue
    if tentativas == 0:
        print("Acesso Bloqueado!")

def empresa_dolly():
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
            print("Seja Bem-Vindo!")
        else:
            tentativas -= 1
            print(f"Você Errou o usuário ou a senha você tem mais {tentativas} tentativas")
            continue
    if tentativas == 0:
        print("Acesso Bloqueado!")



def main():
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
                limpar_tela()
                empresa_dell()
            elif opcao == 2:
                limpar_tela()
                empresa_valle()
            elif opcao == 3:
                limpar_tela()
                empresa_amazon()
            elif opcao == 4:
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
