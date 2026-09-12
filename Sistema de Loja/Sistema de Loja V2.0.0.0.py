#Sistema de Vendas em Uma Loja
#Feito por Lucas Verissimo Yuri Quites e Caio 
#Versão V2.0.0.0

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

limpar_tela()

produtos  = {  
                1: ["Placa de Vídeo", 1650.00], 
                2: ["Bebê Reborn", 20.00],
                3: ["M4a1", 500.00],
                4: ["Free Fire", 10.00],
                5: ["Fortnite", 50.00],
                6: ["Computador", 5000.00],
                7: ["Clash Royale", 20.00],
                8: ["Sabão em Pó", 10.00],
                9: ["Pó", 5.00],
                10: ["Produto KelvinAno", 200000.00]
                                                  }
carrinho = []
preco_total = 0
def inicio():
    while True:

        print("\nSistema de Atendimento Loja:\n")
        print("Bem vindo(a) a Loja KELVEN's!!!\n")
        print("Opção 1: VER PRODUTOS")
        print("Opção 2: COMPRAR")
        print("Opção 3: SAIR\n")
        try:
            opcao = int(input("Digite a Opção Desejada (1-3): \n>  "))
            if opcao == 1:
                limpar_tela()
                ver_produtos()

 
            elif opcao == 2:
                limpar_tela()
                comprar()
                

            elif opcao == 3:
                print("adeus! Que o grandioso Kelvens te abençoe...")
                break
                
            else:
                print("Digite um Valor de Opção Válido! (1-3)")

        except ValueError:
            print("Utilize apenas números para escolher suas opções!")
limpar_tela()


def ver_produtos():
    limpar_tela()
    print("=== === Produtos Disponíveis === ===")
    for codigo, dados in produtos.items():
        print(f"Código: [{codigo}] | {dados[0]:<10} - R${dados[1]:.2f}.")
        print("======================================")
    input("Digite Enter para Sair")
    limpar_tela()

def comprar():
    global preco_total
    limpar_tela()
    print("\n=== ===Setor De Compras=== ===\n")

    try:
        quantidade_itens = int(input("Digite quantos produtos você deseja comprar: \n>  "))

        for i in range(1, quantidade_itens +1):
            while True:
                try:
                    codigo_escolhido = int(input(f"Digite o código  do {i}º produto (número do produto que você deseja comprar): \n>  "))
                    if codigo_escolhido in produtos:
                        produto_nome = produtos[codigo_escolhido][0]
                        produto_preco = produtos[codigo_escolhido][1]
                        carrinho.append(produto_nome)
                        preco_total += produto_preco
                        print(f"-> O produto escolhido foi {produto_nome} e o preço dele é R${produto_preco}")
                        break
                    else:
                        print("Produto Não Enontrado, entre os códigos...")

                except ValueError:
                    print("Entrada Inválida, Digite apenas números")
                    
            if quantidade_itens > 0:
                print(f"Os itens no seu carrinho são {carrinho}")
                print(f"E o preço total desse carrinho é R${preco_total}")
                print(f"Você selecionou {produto_nome} \nseu preço é R${produto_preco:.2f}.")
                confirmar = input(f"Você tem certeza que quer Finalizar esta compra? (Sim/Nao) \n>  ")
                if confirmar == "sim":
                    print(f"Sucesso você comprou {carrinho} no valor total de R${preco_total:.2f}")
                    input("Digite Enter para Sair")
                    break
                            
                elif confirmar == "nao":
                    print(f"Compra Cancelada, Esvaziando carrinho")
                    time.sleep(5)
                    print("Carrinho Esvaziado!")
                    carrinho.clear
                    time.sleep(5)
                    comprar()
                else:
                    print("Opção Inválida, cancelando compra e voltando ao Menu! ")
                    time.sleep(5)
                    limpar_tela()
                    comprar()
    except ValueError:
        print("Entrada inválida. Digite apenas números!")
    print("\n")
    print("Pressione Enter para voltar ao menu.")
    limpar_tela()
    comprar()
limpar_tela()
inicio()