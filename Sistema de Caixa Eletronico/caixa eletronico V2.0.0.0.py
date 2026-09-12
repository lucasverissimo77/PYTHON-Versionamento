#Caixa eletronico V1.0.0.0
#Feito por Caio Mota, Lucas do Vale Verissimo da Costa e Yuri Quites

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear' )

limpar_tela()
time.sleep(0.1)

usuario = input("Qual o nome de usúario: ")
limpar_tela()

dinheiro = 1500

while True:
    try:
        print("Opção1: Consultar saldo")
        print("Opção2: Sacar")
        print("Opção3: Depositar")
        print("Opção4: Sair")
        opcao = int(input(f"{usuario}, Qual opção você deseja? (Escolha de 1-4: )  \n>  "))
        if opcao in (1, 2, 3, 4):
            break
        else:
            print("Por favor, digite apenas números definidos no intervalo: ")
    except ValueError:
        print("Entrada inválida, digite apenas números inteiros: ")
    resposta = input(">  ").strip().lower()

if opcao == 1: 
    def consultar_saldo():
        print(f"\n{usuario} Seu saldo atual é: R${dinheiro:.2f}\n") 
    consultar_saldo() 
        
elif opcao == 2:
    valor = []
    def sacar_dinheiro():
        while True:
            try:
                quantia = float(input(f"{usuario} Qual valor você deseja sacar? (Seu saldo atual é: R${dinheiro:.2f}) \n>  "))
                if valor < [dinheiro] or valor > [dinheiro]:
                    valor.append(quantia)
                    break
                else:
                    print(f"Por favor digite um valor válido entre {dinheiro}  \n>  ")
            except ValueError:
                print("Entrada inválida, digite apenas números...")
                input(">  ").strip().lower()

        novo_valor = dinheiro - quantia
        print(f"Você sacou {quantia} e estava com {dinheiro}!! \nAgora seu saldo em nosso banco é: {novo_valor}")
            
    sacar_dinheiro()

elif opcao == 3:
    valor = []
    def depositar_dinheiro():
        while True:
            try:
                quantia = float(input(f"{usuario}, deposite qualquer quantia: \n>  "))
            except ValueError: 
                print("Entrada inválida, digite apenas números...")
                input(">  ").strip().lower()

        novo_valor = dinheiro + quantia
        print(f"Você depositou {quantia}. Seu novo saldo é: {novo_valor}")
    depositar_dinheiro()     

elif opcao == 4:
    def sair():
        if opcao == 4:
            print("Até logo!")
    sair()
    limpar_tela()