#Sistema de conta de luz
#Feito por Lucas Verissimo
#V6.5.0.0
import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

usuario_salvo = "Lucas" or "Joao_seu_pai"

usuario = input("Digite seu usúario cadastrado: \n>  ")


anus = {
    "Janeiro" : 1,
    "Fevereiro" : 2,
    "Março" : 3,
    "Abril" : 4,
    "Maio" : 5,
    "Junho" : 6,
    "Julho" : 7,
    "Agosto" : 8,
    "Setembro" : 9,
    "Outubro" : 10,
    "Novembro" : 11,
    "Dezembro" : 12,
}
valores = {
    130.00 : 144.4,
    130.00 : 144.4,
    120.00 : 133.3,
    110.00 : 122.2,
    100.00 : 111.1,
    95.00 : 105.6,
    95.00 : 105.6,
    100.00 : 111.1,
    110.00 : 122.2,
    115.00 : 127.8,
    120.00 : 133.3,
    125.00 : 138.9,
}


def sistema_luz():

    for meses, meses_num in anus.items():
        print(f"- {meses.title()} mês {meses_num} -")
        print("-------------------------------------")

    
    while 0 < meses_num <= 12:
        try:
            meses_num = int(input("Insira o mês (1-12) que o senhor quer saber a sua conta ou zero para saber mais do menu de Opções \n>  "))
            if meses_num == 1:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$130.00")
                valor = 130.00
                resposta = input(f"{usuario} o senhor quer pagar sua dívida de {valor:.2f} agora? (Sim/Não) \n>  ")
                if resposta.lower() == "sim":
                    limpar_tela()
                    print("\n ---Setor de Pagamento--- \n")
                    print("Opção 1: Débito")
                    print("Opçao 2: Crédito")
                    print("Opção 3: Pix")
                    print("Opção 4: Dinheiro")
                    print("Opção 5: Sair")
                    opcao = int(input("Digite o número da opção [1-5]"))
                    if opcao == 1:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 2:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 3:
                        print(f"cole esta chave aleatoria para pagar o valor de R${valor} no seu aplicativo de banco: uihqfeuyqfeuyeqhyfqgeyfgyuqheuifjiu9qhu3gfry8qgy8fguqh3ifjqi03jhfi8hqhf789q3hfhqhf8qij3fi9qj390fu8q3y78rft76y812uyy")
                        time.sleep(1)
                    if opcao == 4:
                        print(f"Procure uma unidade válida para pagar em dinheiro este valor: R${valor}")
                        time.sleep(1)
                    if opcao == 5:
                        print(f"Até logo, Adeus cliente {usuario}.")
                        time.sleep(1)
                    time.sleep(1)
                    limpar_tela()
                    continue
                limpar_tela()
            
            elif meses_num == 2:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$130.00")
                valor = 130.00
                resposta = input(f"{usuario} o senhor quer pagar sua dívida de {valor:.2f} agora? (Sim/Não) \n>  ")
                if resposta.lower() == "sim":
                    limpar_tela()
                    print("\n ---Setor de Pagamento--- \n")
                    print("Opção 1: Débito")
                    print("Opçao 2: Crédito")
                    print("Opção 3: Pix")
                    print("Opção 4: Dinheiro")
                    print("Opção 5: Sair")
                    opcao = int(input("Digite o número da opção [1-5]"))
                    if opcao == 1:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 2:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 3:
                        print(f"cole esta chave aleatoria para pagar o valor de R${valor} no seu aplicativo de banco: uihqfeuyqfeuyeqhyfqgeyfgyuqheuifjiu9qhu3gfry8qgy8fguqh3ifjqi03jhfi8hqhf789q3hfhqhf8qij3fi9qj390fu8q3y78rft76y812uyy")
                        time.sleep(1)
                    if opcao == 4:
                        print(f"Procure uma unidade válida para pagar em dinheiro este valor: R${valor}")
                        time.sleep(1)
                    if opcao == 5:
                        print(f"Até logo, Adeus cliente {usuario}.")
                        time.sleep(1)
                    time.sleep(1)
                    limpar_tela()
                    continue
                limpar_tela()
            
            elif meses_num == 3:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$120.00")
                valor = 120.00
                resposta = input(f"{usuario} o senhor quer pagar sua dívida de {valor:.2f} agora? (Sim/Não) \n>  ")
                if resposta.lower() == "sim":
                    limpar_tela()
                    print("\n ---Setor de Pagamento--- \n")
                    print("Opção 1: Débito")
                    print("Opçao 2: Crédito")
                    print("Opção 3: Pix")
                    print("Opção 4: Dinheiro")
                    print("Opção 5: Sair")
                    opcao = int(input("Digite o número da opção [1-5]"))
                    if opcao == 1:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 2:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 3:
                        print(f"cole esta chave aleatoria para pagar o valor de R${valor} no seu aplicativo de banco: uihqfeuyqfeuyeqhyfqgeyfgyuqheuifjiu9qhu3gfry8qgy8fguqh3ifjqi03jhfi8hqhf789q3hfhqhf8qij3fi9qj390fu8q3y78rft76y812uyy")
                        time.sleep(1)
                    if opcao == 4:
                        print(f"Procure uma unidade válida para pagar em dinheiro este valor: R${valor}")
                        time.sleep(1)
                    if opcao == 5:
                        print(f"Até logo, Adeus cliente {usuario}.")
                        time.sleep(1)
                    time.sleep(1)
                    limpar_tela()
                    continue
                limpar_tela()
            
            elif meses_num == 4:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$110.00")
                valor = 110.00
                resposta = input(f"{usuario} o senhor quer pagar sua dívida de {valor:.2f} agora? (Sim/Não) \n  ")
                if resposta.lower() == "sim":
                    limpar_tela()
                    print("\n ---Setor de Pagamento--- \n")
                    print("Opção 1: Débito")
                    print("Opçao 2: Crédito")
                    print("Opção 3: Pix")
                    print("Opção 4: Dinheiro")
                    print("Opção 5: Sair")
                    opcao = int(input("Digite o número da opção [1-5]"))
                    if opcao == 1:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 2:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 3:
                        print(f"cole esta chave aleatoria para pagar o valor de R${valor} no seu aplicativo de banco: uihqfeuyqfeuyeqhyfqgeyfgyuqheuifjiu9qhu3gfry8qgy8fguqh3ifjqi03jhfi8hqhf789q3hfhqhf8qij3fi9qj390fu8q3y78rft76y812uyy")
                        time.sleep(1)
                    if opcao == 4:
                        print(f"Procure uma unidade válida para pagar em dinheiro este valor: R${valor}")
                        time.sleep(1)
                    if opcao == 5:
                        print(f"Até logo, Adeus cliente {usuario}.")
                        time.sleep(1)
                    time.sleep(1)
                    limpar_tela()
                    continue
                limpar_tela()
            
            elif meses_num == 5:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$100.00")
                valor = 100.00
                resposta = input(f"{usuario} o senhor quer pagar sua dívida de {valor:.2f} agora? (Sim/Não) \n>  ")
                if resposta.lower() == "sim":
                    limpar_tela()
                    print("\n ---Setor de Pagamento--- \n")
                    print("Opção 1: Débito")
                    print("Opçao 2: Crédito")
                    print("Opção 3: Pix")
                    print("Opção 4: Dinheiro")
                    print("Opção 5: Sair")
                    opcao = int(input("Digite o número da opção [1-5] \n>  "))
                    if opcao == 1:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 2:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 3:
                        print(f"cole esta chave aleatoria para pagar o valor de R${valor} no seu aplicativo de banco: uihqfeuyqfeuyeqhyfqgeyfgyuqheuifjiu9qhu3gfry8qgy8fguqh3ifjqi03jhfi8hqhf789q3hfhqhf8qij3fi9qj390fu8q3y78rft76y812uyy")
                        time.sleep(1)
                    if opcao == 4:
                        print(f"Procure uma unidade válida para pagar em dinheiro este valor: R${valor}")
                        time.sleep(1)
                    if opcao == 5:
                        print(f"Até logo, Adeus cliente {usuario}.")
                        time.sleep(1)
                    time.sleep(1)
                    limpar_tela()
                    continue
                limpar_tela()
            
            elif meses_num == 6:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$95.00")
                valor = 95.00
                resposta = input(f"{usuario} o senhor quer pagar sua dívida de {valor:.2f} agora? (Sim/Não) \n>  ")
                if resposta.lower() == "sim":
                    limpar_tela()
                    print("\n ---Setor de Pagamento--- \n")
                    print("Opção 1: Débito")
                    print("Opçao 2: Crédito")
                    print("Opção 3: Pix")
                    print("Opção 4: Dinheiro")
                    print("Opção 5: Sair")
                    opcao = int(input("Digite o número da opção [1-5] \n>  "))
                    if opcao == 1:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 2:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 3:
                        print(f"cole esta chave aleatoria para pagar o valor de R${valor} no seu aplicativo de banco: uihqfeuyqfeuyeqhyfqgeyfgyuqheuifjiu9qhu3gfry8qgy8fguqh3ifjqi03jhfi8hqhf789q3hfhqhf8qij3fi9qj390fu8q3y78rft76y812uyy")
                        time.sleep(1)
                    if opcao == 4:
                        print(f"Procure uma unidade válida para pagar em dinheiro este valor: R${valor}")
                        time.sleep(1)
                    if opcao == 5:
                        print(f"Até logo, Adeus cliente {usuario}.")
                        time.sleep(1)
                    time.sleep(1)
                    limpar_tela
                    continue
                limpar_tela()
            
            elif meses_num == 7:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$95.00")
                valor = 95.00
                resposta = input(f"{usuario} o senhor quer pagar sua dívida de {valor:.2f} agora? (Sim/Não) \n>  ")
                if resposta.lower() == "sim":
                    limpar_tela()
                    print("\n ---Setor de Pagamento--- \n")
                    print("Opção 1: Débito")
                    print("Opçao 2: Crédito")
                    print("Opção 3: Pix")
                    print("Opção 4: Dinheiro")
                    print("Opção 5: Sair")
                    opcao = int(input("Digite o número da opção [1-5] \n>  "))
                    if opcao == 1:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 2:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 3:
                        print(f"cole esta chave aleatoria para pagar o valor de R${valor} no seu aplicativo de banco: uihqfeuyqfeuyeqhyfqgeyfgyuqheuifjiu9qhu3gfry8qgy8fguqh3ifjqi03jhfi8hqhf789q3hfhqhf8qij3fi9qj390fu8q3y78rft76y812uyy")
                        time.sleep(1)
                    if opcao == 4:
                        print(f"Procure uma unidade válida para pagar em dinheiro este valor: R${valor}")
                        time.sleep(1)
                    if opcao == 5:
                        print(f"Até logo, Adeus cliente {usuario}.")
                        time.sleep(1)
                    time.sleep(1)
                    limpar_tela()
                    continue
                limpar_tela()
            
            elif meses_num == 8:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$100.00")
                valor = 100.00
                resposta = input(f"{usuario} o senhor quer pagar sua dívida de {valor:.2f} agora? (Sim/Não) \n>  ")
                if resposta.lower() == "sim":
                    limpar_tela()
                    print("\n ---Setor de Pagamento--- \n")
                    print("Opção 1: Débito")
                    print("Opçao 2: Crédito")
                    print("Opção 3: Pix")
                    print("Opção 4: Dinheiro")
                    print("Opção 5: Sair")
                    opcao = int(input("Digite o número da opção [1-5] \n>  "))
                    if opcao == 1:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 2:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 3:
                        print(f"cole esta chave aleatoria para pagar o valor de R${valor} no seu aplicativo de banco: uihqfeuyqfeuyeqhyfqgeyfgyuqheuifjiu9qhu3gfry8qgy8fguqh3ifjqi03jhfi8hqhf789q3hfhqhf8qij3fi9qj390fu8q3y78rft76y812uyy")
                        time.sleep(1)
                    if opcao == 4:
                        print(f"Procure uma unidade válida para pagar em dinheiro este valor: R${valor}")
                        time.sleep(1)
                    if opcao == 5:
                        print(f"Até logo, Adeus cliente {usuario}.")
                        time.sleep(1)
                    time.sleep(1)
                    limpar_tela()
                    continue
                limpar_tela()
            
            elif meses_num == 9:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$110.00")
                valor = 110.00
                resposta = input(f"{usuario} o senhor quer pagar sua dívida de {valor:.2f} agora? (Sim/Não) \n>  ")
                if resposta.lower() == "sim":
                    limpar_tela()
                    print("\n ---Setor de Pagamento--- \n")
                    print("Opção 1: Débito")
                    print("Opçao 2: Crédito")
                    print("Opção 3: Pix")
                    print("Opção 4: Dinheiro")
                    print("Opção 5: Sair")
                    opcao = int(input("Digite o número da opção [1-5] \n>  "))
                    if opcao == 1:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 2:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 3:
                        print(f"cole esta chave aleatoria para pagar o valor de R${valor} no seu aplicativo de banco: uihqfeuyqfeuyeqhyfqgeyfgyuqheuifjiu9qhu3gfry8qgy8fguqh3ifjqi03jhfi8hqhf789q3hfhqhf8qij3fi9qj390fu8q3y78rft76y812uyy")
                        time.sleep(1)
                    if opcao == 4:
                        print(f"Procure uma unidade válida para pagar em dinheiro este valor: R${valor}")
                        time.sleep(1)
                    if opcao == 5:
                        print(f"Até logo, Adeus cliente {usuario}.")
                        time.sleep(1)
                    time.sleep(1)
                    limpar_tela()
                    continue
                limpar_tela()
            
            elif meses_num == 10:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$115.00")
                valor = 115.00
                resposta = input(f"{usuario} o senhor quer pagar sua dívida de {valor:.2f} agora? (Sim/Não) \n>  ")
                if resposta.lower() == "sim":
                    limpar_tela()
                    print("\n ---Setor de Pagamento--- \n")
                    print("Opção 1: Débito")
                    print("Opçao 2: Crédito")
                    print("Opção 3: Pix")
                    print("Opção 4: Dinheiro")
                    print("Opção 5: Sair")
                    opcao = int(input("Digite o número da opção [1-5] \n>  "))
                    if opcao == 1:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 2:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 3:
                        print(f"cole esta chave aleatoria para pagar o valor de R${valor} no seu aplicativo de banco: uihqfeuyqfeuyeqhyfqgeyfgyuqheuifjiu9qhu3gfry8qgy8fguqh3ifjqi03jhfi8hqhf789q3hfhqhf8qij3fi9qj390fu8q3y78rft76y812uyy")
                        time.sleep(1)
                    if opcao == 4:
                        print(f"Procure uma unidade válida para pagar em dinheiro este valor: R${valor}")
                        time.sleep(1)
                    if opcao == 5:
                        print(f"Até logo, Adeus cliente {usuario}.")
                        time.sleep(1)
                    time.sleep(1)
                    limpar_tela()
                    continue
                limpar_tela()
            
            elif meses_num == 11:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$120.00")
                valor = 120.00
                resposta = input(f"{usuario} o senhor quer pagar sua dívida de {valor:.2f} agora? (Sim/Não) \n>  ")
                if resposta.lower() == "sim":
                    limpar_tela()
                    print("\n ---Setor de Pagamento--- \n")
                    print("Opção 1: Débito")
                    print("Opçao 2: Crédito")
                    print("Opção 3: Pix")
                    print("Opção 4: Dinheiro")
                    print("Opção 5: Sair")
                    opcao = int(input("Digite o número da opção [1-5] \n>  "))
                    if opcao == 1:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 2:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 3:
                        print(f"cole esta chave aleatoria para pagar o valor de R${valor} no seu aplicativo de banco: uihqfeuyqfeuyeqhyfqgeyfgyuqheuifjiu9qhu3gfry8qgy8fguqh3ifjqi03jhfi8hqhf789q3hfhqhf8qij3fi9qj390fu8q3y78rft76y812uyy")
                        time.sleep(1)
                    if opcao == 4:
                        print(f"Procure uma unidade válida para pagar em dinheiro este valor: R${valor}")
                        time.sleep(1)
                    if opcao == 5:
                        print(f"Até logo, Adeus cliente {usuario}.")
                        time.sleep(1)
                    time.sleep(1)
                    limpar_tela()
                    continue
                limpar_tela()
            
            elif meses_num == 12:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$125.00")
                valor = 125.00
                resposta = input(f"{usuario} o senhor quer pagar sua dívida de {valor:.2f} agora? (Sim/Não) \n>  ")
                if resposta.lower() == "sim":
                    limpar_tela()
                    print("\n ---Setor de Pagamento--- \n")
                    print("Opção 1: Débito")
                    print("Opçao 2: Crédito")
                    print("Opção 3: Pix")
                    print("Opção 4: Dinheiro")
                    print("Opção 5: Sair")
                    opcao = int(input("Digite o número da opção [1-5] \n>  "))
                    if opcao == 1:
                        print(f"Adicione seu cartão de Débito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 2:
                        print(f"Adicione seu cartão de crédito via aplicativo e pague R${valor}  por lá, ou em uma instituição próxima")
                        time.sleep(1)
                    if opcao == 3:
                        print(f"cole esta chave aleatoria para pagar o valor de R${valor} no seu aplicativo de banco: uihqfeuyqfeuyeqhyfqgeyfgyuqheuifjiu9qhu3gfry8qgy8fguqh3ifjqi03jhfi8hqhf789q3hfhqhf8qij3fi9qj390fu8q3y78rft76y812uyy")
                        time.sleep(1)
                    if opcao == 4:
                        print(f"Procure uma unidade válida para pagar em dinheiro este valor: R${valor}")
                        time.sleep(1)
                    if opcao == 5:
                        print(f"Até logo, Adeus cliente {usuario}.")
                        time.sleep(1)
                    time.sleep(1)
                    limpar_tela()
                    continue
                limpar_tela()
                
            elif meses_num == 0:
                limpar_tela()
                print("\n ---Tela de opções adicionais--- \n")
                print("Opção 1: Calcular média de todos os meses")
                print("Opção 2: Somar o total de Valores que o senhor deve")
                print("Opção 3: Ver o consumo e o valor de cada mês")
                mais_resposta = int(input("Digite a Opção que deseja: \n>  "))
                if mais_resposta == 1:
                    limpar_tela()
                    for preco, consumo in valores.items():
                        print(f"---{meses}: {consumo:.2f}kWh R${preco}")
                        print("------------------------------------")
                    media = preco / 12
                    print(f"A média de valor é {media}")
                    time.sleep(5)
                    limpar_tela()
                    continue
                if mais_resposta == 2:
                    limpar_tela()
                    print("---Somatório---")
                    for preco, consumo in valores.items():
                        print(f"---{meses}: {consumo:.2f}kWh R${preco}")
                        print("------------------------------------")
                    soma = preco * 12
                    print(f"O somatório de quanto você deve é: R${soma}")
                    time.sleep(5)
                    limpar_tela()
                    continue
                if mais_resposta == 3:
                    limpar_tela()
                    print("Quadro de consumo")
                    for preco, consumo in valores.items():
                        print(f"---{meses}: {consumo:.2f}kWh R${preco}")
                        print("------------------------------------")
                    time.sleep(5)
                    limpar_tela()
                    continue
                continue


            else:
                print("Entrada inválida, Digite apenas números no intervalo de (1-12): ")
            
        except ValueError:
            print("\nError 404, Use apenas números inteiros seu animal .-.\n")
sistema_luz()