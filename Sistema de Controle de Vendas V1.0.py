#Sistema de Controle de Vendas
#Feito por Lucas Verissimo
#Versão 1.0.0.0

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

qntd_venda = 0
vendas_totais = []

funcionarios_loja = {
    "F0001" : "Lucas",
    "F0002" : "Yuri",
    "F0003" : "Caio",
    "F0004" : "Kelvems",
    "F0005" : "Matias",
    "F0006" : "Salles",
}   #Código : "Funcionario/Clts"

def vender():
    global vendas_totais
    global qntd_venda
    print("\n~~~Caixa da Loja~~~\n")
    while True:
        try:
            print("Digite o valor da venda ou 0 para sair")
        
            venda = float(input(">  "))
            if venda > 0:
                vendas_totais.append(venda)
                qntd_venda += 1
            if venda == 0:
                print("Saindo...")
                time.sleep(2.5)
                main()
        except ValueError:
            print("Entrada inválida, Digite apenas caractéres válidos!!")

def opcao1():
    global codigo
    limpar_tela()
    print("=== ===Código e Funcionarios=== ===")
    for codigo, clts in funcionarios_loja.items():
        print("="*25)
        print(f"Código: {codigo} | Funcionario: {clts}")
    print("Aperte Enter para voltar ao Menu inicial")
    input(">  ")
    time.sleep(2.5)
    
def opcao2():
    global resposta_codigo
    limpar_tela()
    print("---Confirmação Funcionario---")
    tentativas = 3
    while tentativas > 0:
        print("Digite o código do Vendedor para acessar o caixa da loja: (Diferença de Letras Maiúsculas de Minúsculas)")
        resposta_codigo = input(">  ").strip().upper()
        if resposta_codigo in funcionarios_loja:
            print("Acesso Liberado")
            print("Carregando...")
            time.sleep(0.5)
            tentativas = 3
            limpar_tela()
            vender()
        else:
            tentativas -= 1
            print(f"Acesso Recusado, tente novamente você tem mais {tentativas} tentativas...")
        if tentativas == 0:
            print("Acesso Bloqueado!!")
            tentativas = 0
            break

def opcao3():
    if qntd_venda > 0:
        print("\n><><Resultados><><\n")
        media = sum(vendas_totais) / qntd_venda
        preco_total = sum(vendas_totais)
        print(f"A média de preços de produtos vendidos de hoje é {media:.2f}")
        print(f"O preço total recebido hoje foi R${preco_total:.2f}")
        print(f"O Código do vendedor de hoje foi {resposta_codigo}")
        print("Digite ENTER para sair: ")
        input(">  ")
    else:
        print("Você não passou nenhum produto no caixa")
        time.sleep(5)

def main():
    global vendas_totais
    global qntd_venda
    global resposta_codigo
    while True:
        limpar_tela()
        print("\n<><>Sistema de Loja<><>")
        print("Opção 1: Ver códigos e funcionarios")
        print("Opção 2: Caixa da Loja")
        print("Opção 3: Resultados")
        print("Opção 4: Sair\n")
        print("Escolha uma Opção (Resposta deve ser no valor da Opção (1-4))")
        try:
            resposta_opcao = int(input(">  "))
            if resposta_opcao == 1:
                opcao1()
            elif resposta_opcao == 2:
                opcao2()
            elif resposta_opcao == 3:
                opcao3()
            elif resposta_opcao == 4:
                print("Aperte Enter para sair: ")
                input(">  ")
            else:
                print("Opção Inválida Tente Novamente! ")
        except ValueError:
                print("Digite apenas caracteres válidos")
                continue
main()

