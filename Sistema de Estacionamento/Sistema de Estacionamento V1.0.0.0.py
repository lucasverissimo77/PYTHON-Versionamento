#Sistema de Estacionamento
#Feito por Lucas Verissimo
#Versão 1.0.0.0

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

placa_moto = ["ABC-1234", "XYZ-9876", "LMN-4567", "QWE-8520", "RTS-3019"]
placa_carro = ["JKL-7789", "POI-6423", "VBN-1357", "HGF-9081", "ZXC-2745"]
preco_padrao_moto = 10.00
preco_padrao_carro = 15.00
preco = 0

def estacionamento():
    global preco
    while True:
        try:
            print("Boas-Vindas ao nosso Estacionamento, O que deseja ?\n")
            print("Opção 1: Estou com dúvidas.")
            print("Opção 2: Quero estacionar meu carro/moto.")
            print("Opção 3: Quero pagar meu estacionamento.")
            print("Opção 4: Sair.")
            resposta_inicial = int(input("Qual opção o senhor deseja? (1-4) \n>  "))
            if resposta_inicial == 1:
                limpar_tela()
                print("\n--- ---Fórum de Dúvidas--- ---\n")
                print("Pesquise em nosso site. www.xestacionamentos.com.usa")
                print("Deseja mais alguma coisa? (Sim/Não)")
                escolha = input(">  ").strip().lower()
                if escolha == "sim":
                    limpar_tela()
                    continue
                if escolha == "nao":
                    print("Obrigado por não utilizar nosso sistema!")
                    break
                else:
                    print("Digite uma Opção válida! retornando ao menu...")
                    time.sleep(2)
                    limpar_tela()

            elif resposta_inicial == 2:
                limpar_tela()
                print("--- ---Sistema de cadastro de carros/motos--- ---")
                print("Para cadastrarmos seu carro/moto digite o seu nome")
                nome = input(">  ").strip().lower()
                print(f"Olá {nome}, Precisamos saber se seu veículo é um carro ou uma moto:")
                escolha = input(">  ").strip().lower()
                if escolha == "carro":
                    limpar_tela()
                    print("\n=== ===Cadastro de carro=== ===\n")
                    print("Digite a placa do carro: ")
                    resposta_placa = input(">  ").strip()
                    placa_carro.append(resposta_placa)
                    print("carregando...")
                    time.sleep(5)
                    limpar_tela()
                    print("\n--- ---Quantidade de Horas--- ---\n")
                    print("Opção 1: Até 1 Hora.")
                    print("Opção 2: De 1 Horas até 3 Horas.")
                    print("Opção 3: Mais de 3 Horas.")
                    print("Opção 4: Voltar ao início.")
                    print(f"Qual opção deseja escolher para seu veiculo de identificação {resposta_placa}? (1-4)")
                    resposta_horas = int(input(">  ").strip())
                    if resposta_horas == 1:
                        print("O valor de até uma hora no estacionamento é de: R$8.00")
                        preco = 8.00
                        print(f"O senhor {nome} Deseja estacionar o seu carro? Está de acordo com o preço??")
                        respostas = input(">  ").strip().lower()
                        if respostas == 'sim':
                            print("Carregando")
                            time.sleep(5)
                            print(f"Entrada Liberada, pode entrar com o seu {escolha}.")
                            print("Carregando")
                            time.sleep(5)
                            continue
                        if respostas == "nao":
                            print("Carregando")
                            time.sleep(5)
                            print("Saindo do sistema! ")
                            limpar_tela()
                            continue
                    if resposta_horas == 2:
                        print("O valor de 1 hora até 3 horas no estacionamento é de: R$15.00")
                        preco = 15.00
                        print(f"O senhor {nome} Deseja estacionar o seu carro? Está de acordo com o preço??")
                        respostas = input(">  ").strip().lower()
                        if respostas == 'sim':
                            print("Carregando")
                            time.sleep(5)
                            print(f"Entrada Liberada, pode entrar com o seu {escolha}.")
                            print("Carregando")
                            time.sleep(5)
                            continue
                        if respostas == "nao":
                            print("Carregando")
                            time.sleep(5)
                            print("Saindo do sistema! ")
                            limpar_tela()
                            continue
                    if resposta_horas == 3:
                        print("O valor de mais de 3 horas no estacionamento é de: R$20.00")
                        preco = 20.00
                        print(f"O senhor {nome} Deseja estacionar o seu carro? Está de acordo com o preço??")
                        respostas = input(">  ").strip().lower()
                        if respostas == 'sim':
                            print("Carregando")
                            time.sleep(5)
                            print(f"Entrada Liberada, pode entrar com o seu {escolha}.")
                            print("Carregando")
                            time.sleep(5)
                            continue
                        if respostas == "nao":
                            print("Carregando")
                            time.sleep(5)
                            print("Saindo do sistema! ")
                            limpar_tela()
                            continue
                    if resposta_horas == 4:
                        print("Carregando...")
                        time.sleep(5)
                        limpar_tela()
                        continue
                if escolha == "moto":
                    limpar_tela()
                    print("\n=== ===Cadastro de Moto=== ===\n")
                    print("Digite a placa do carro: ")
                    resposta_placa = input(">  ").strip()
                    placa_moto.append(resposta_placa)
                    print("Carregando...")
                    time.sleep(5)
                    limpar_tela()
                    print("\n--- ---Quantidade de Horas--- ---\n")
                    print("Opção 1: Até 1 Hora.")
                    print("Opção 2: De 1 Horas até 3 Horas.")
                    print("Opção 3: Mais de 3 Horas.")
                    print("Opção 4: Voltar ao início.")
                    print(f"Qual opção deseja escolher para seu veiculo de identificação {resposta_placa}? (1-4)")
                    resposta_horas = int(input(">  ").strip())
                    if resposta_horas == 1:
                        print("O valor de até uma hora no estacionamento é de: R$8.00")
                        preco = 8.00
                        print(f"O senhor {nome} Deseja estacionar a sua moto? Está de acordo com o preço??")
                        respostas = input(">  ").strip().lower()
                        if respostas == 'sim':
                            print("Carregando")
                            time.sleep(5)
                            print(f"Entrada Liberada, pode entrar com a sua {escolha}.")
                            print("Carregando")
                            time.sleep(5)
                            continue
                        if respostas == "nao":
                            print("Carregando")
                            time.sleep(5)
                            print("Saindo do sistema! ")
                            limpar_tela()
                            continue
                    if resposta_horas == 2:
                        print("O valor de 1 hora até 3 horas no estacionamento é de: R$15.00")
                        preco = 15.00
                        print(f"O senhor {nome} Deseja estacionar a sua moto? Está de acordo com o preço??")
                        respostas = input(">  ").strip().lower()
                        if respostas == 'sim':
                            print("Carregando")
                            time.sleep(5)
                            print(f"Entrada Liberada, pode entrar com a sua {escolha}.")
                            print("Carregando")
                            time.sleep(5)
                            continue
                        if respostas == "nao":
                            print("Carregando")
                            time.sleep(5)
                            print("Saindo do sistema! ")
                            limpar_tela()
                            continue
                        
                    if resposta_horas == 3:
                        print("O valor de mais de 3 horas no estacionamento é de: R$20.00")
                        preco = 20.00
                        print(f"O senhor {nome} Deseja estacionar a sua moto? Está de acordo com o preço??")
                        respostas = input(">  ").strip().lower()
                        if respostas == 'sim':
                            print("Carregando")
                            time.sleep(5)
                            print(f"Entrada Liberada, pode entrar com a sua {escolha}.")
                            print("Carregando")
                            time.sleep(5)
                            continue
                        if respostas == "nao":
                            print("Carregando")
                            time.sleep(5)
                            print("Saindo do sistema! ")
                            limpar_tela()
                            continue
                    if resposta_horas == 4:
                        print("Carregando...")
                        time.sleep(5)
                        continue
            elif resposta_inicial == 3:
                limpar_tela()
                print("\n--- ---Sistema de Pagamento--- ---\n")
                print("Para sabermos o valor que o senhor deve pagar, devemos saber seu veiculo. (Carro/Moto)")
                escolha = input(">  ").strip().lower()
                if escolha == "moto":
                    limpar_tela()
                    print("\n--- ---Estacionamento de Moto--- ---\n")
                    print("Para sabermos o valor, digite a placa do seu veículo (Letras Maiúsculas - Números): ")
                    resposta_placa = input(">  ").strip()
                    if resposta_placa in placa_moto:
                        valor_final = preco if preco > 0 else preco_padrao_moto
                        print(f"Sua placa é: {resposta_placa} e o valor que você deve é R${valor_final}: ")
                        print("Para pagar o que o senhor deve ao estacionamento vá ao guichê mais próximo.")
                        input("Aperte Enter para voltar ao menu: \n>  ")
                        limpar_tela()
                    else:
                        print("Placa não encontrada")
                        time.sleep(2)
                        print("Voltando ao Menu")
                        time.sleep(2)
                        continue
                if escolha == "carro":
                    limpar_tela()
                    print("\n--- ---Estacionamento de Carros--- ---\n")
                    print("Para sabermos o valor, digite a placa do seu veículo (Letras Maiúsculas - Números): ")
                    resposta_placa = input(">  ").strip()
                    if resposta_placa in placa_carro:
                        valor_final = preco if preco > 0 else preco_padrao_carro
                        print(f"Sua placa é: {resposta_placa} e o valor que você deve é R${valor_final}:")
                        print("Para pagar o que o senhor deve ao estacionamento vá ao guichê mais próximo.")
                        input("Aperte Enter para voltar ao menu: \n>  ")
                        limpar_tela()
                    else:
                        print("Placa não encontrada")
                        time.sleep(2)
                        print("Voltando ao Menu")
                        time.sleep(2)
                        continue
            elif resposta_inicial == 4:
                print("Saindo do Sistema")
                input("Digite Enter para sair \n>  ")
                time.sleep(2)
                limpar_tela()
                break
            else:
                print("Digite uma Opção válida de 1 a 4!")
                time.sleep(2)
                limpar_tela()
        except ValueError:
            print("Erro de Resposta, Insira Apenas Números inteiros")
            time.sleep(5)
            limpar_tela()

estacionamento()