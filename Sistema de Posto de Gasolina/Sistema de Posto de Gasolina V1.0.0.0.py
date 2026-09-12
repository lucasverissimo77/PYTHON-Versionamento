#Sistema de Posto de Gasolina
#Feito por Lucas Verissimo
#Versão 1.0.0.0

import os
import time


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)


gasolina = 0
gasolina_moto_max = 16
gasolina_carro_max = 60
preco = 5.00

while True:
    try:
        print("\n--- --- Posto de Gasolina --- ---\n")
        print("Seja Bem vindo ao nosso posto de gasolina como podemos ajudar (1/2) ?")
        print("Opção 1: Abastecer")
        print("Opção 2: Sair")
        resposta_principal = int(input(">  ").strip().lower())
        while resposta_principal == 2:
            limpar_tela()
            print("\n--- ---Tela de Desligamento--- ---\n")
            input("Aperte qualquer tecla para o desligamento. \n>  ")
            break
        while resposta_principal == 1:
            limpar_tela()
            print("\n--- ---Tela de Abastecimento--- ---\n")
            print("Qual é seu veiculo? (Carro/Moto | Apenas)")
            veiculo = input(">  ").strip().lower()
            if veiculo == "moto":
                print(f"O seu Veiculo é {veiculo}, e a quantidade de litro maxima deste veiculo é {gasolina_moto_max} Litros")
                print(f"O litro de gasolina está 5 reais em nosso posto\n")
                gasolina = int(input(f"Digite quantos litros você quer abastecer em sua {veiculo} \n>  "))
                if gasolina <= gasolina_moto_max:
                    print(f"Você abasteceu {gasolina} Litros.")
                    preco_moto = gasolina * 5
                    print(f"O valor do abastecimento foi de R${preco_moto:.2f}")
                    break
                else:
                    print(f"Você está abastecendo mais que sua {veiculo} aguenta")
                    time.sleep(5)
                    continue
            if veiculo == "carro":
                print(f"O seu Veiculo é {veiculo}, e a quantidade de litro maxima deste veiculo é {gasolina_carro_max} Litros")
                print(f"O litro de gasolina está 5 reais em nosso posto\n")
                gasolina = int(input(f"Digite quantos litros você quer abastecer em sua {veiculo} \n>  "))
                if gasolina <= gasolina_moto_max:
                    print(f"Você abasteceu {gasolina} Litros.")
                    preco_carro = gasolina * 5
                    print(f"O valor do abastecimento foi de R${preco_carro:.2f}")
                    break
                else:
                    print(f"Você está abastecendo mais que seu {veiculo} aguenta")
                    time.sleep(5)
                    continue
                    
    except ValueError:
        print("Entrada inválida, digite apenas números inteiros quando for pedido.")
