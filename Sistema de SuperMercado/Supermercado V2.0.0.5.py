# Supermercado
# Feito por Lucas do Vale Verissimo
# V1.0.0.1

catalogo = {
    "banana" : 4.50,
    "coca cola" : 8.00,
    "prudence" : 12.00,
    "chocolate" : 6.00,
    "pepsi" : 7.00,
    "programa_lixo" : 100.00,
}
preco_obtido = 100.00
usuario_adm = "lucas"

while True:
    try:
        # Sistema de menu para boas vindas e escolhas iniciais
        print("\nSeja Bem-Vindo a nossa loja online! O senhor já faz parte de nosso sistema? (Sim/Nao/Adm)")
        resposta_inicial = input("> ").strip().lower()

        while resposta_inicial not in ("sim", "nao", "adm"):
            print("Resposta inválida. Digite apenas Sim, Não ou Adm.")
            resposta_inicial = input("> ").strip().lower()

        # CASO A PESSOA RESPONDA SIM
        if resposta_inicial == "sim":
            usuario = input("Qual seu nome de usuário?: \n> ").strip().lower()
            print("\n  ---Produtos disponiveis---  ")
            for produtos, precos in catalogo.items():
                print(f"- {produtos.title()}: R$ {precos:.2f}")
                print("--------------------------\n")
            
            quantidade = int(input("Quantos itens deseja comprar? \nOu digite (0) Para sair do sistema. \n> "))
            
            if quantidade == 0:
                print("Até logo!!")
                break
            elif quantidade > 0:
                # Agora o fluxo de escolha faz sentido aqui dentro
                escolha = input("O que você deseja comprar? \n> ").strip().lower()
                if escolha in catalogo:
                    preco_unitario = catalogo[escolha]
                    valor_total = preco_unitario * quantidade

                    print(f"\nSucesso! Você comprou {quantidade}x{escolha.title()}.")
                    print(f"Valor unitário: R${preco_unitario:.2f}.")
                    print(f"Valor total da compra R${valor_total}")
                else:
                    print("Produto não encontrado no catálogo")
                    break
            else:
                print("Por favor, digite um número maior que zero ou (0) para sair!")

        # CASO A PESSOA RESPONDA NAO
        elif resposta_inicial == "nao":
            print("Por favor, crie uma conta primeiro ou contacte o suporte. Até logo!")
            break

        # SE O USUÁRIO FOR ADMIN DO MERCADO
        elif resposta_inicial == "adm":
            usuario_salvo = input("Diga seu nome de usuário (credencial de adm): \n> ").strip().lower()
            
            if usuario_salvo == usuario_adm:
                print("\nSeja bem-vindo dono do mercado, meu herói, meu dono, meu criador...")
                print("O que o senhor quer fazer hoje?")
                print("Opção 1: Ver produtos criados")
                print("Opção 2: Ver dinheiro arrecadado")
                print("Opção 3: Ver o nome do seu negócio")
                print("Opção 4: Sair")
                
                opcao_adm = input("\nEscolha uma opção... \n> ").strip()
                
                while opcao_adm not in ("1", "2", "3", "4"):
                    print("Por favor, digite apenas os números das opções válidas (1 a 4).")
                    opcao_adm = input("> ").strip()

                if opcao_adm == "1":
                    print(f"Produtos: {produtos}")
                elif opcao_adm == "2":
                    print(f"Dinheiro em caixa: R$ {preco_obtido:.2f}")
                elif opcao_adm == "3":
                    print("Del Valle Company --- Quem é tu rapa que não sabe o nome da empresa, to de olho ein!!")
                elif opcao_adm == "4":
                    print("Até logo, chefe!")
                    break
            else:
                print("Saia daqui imediatamente! Credenciais incorretas.")
                break

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros onde for solicitado.")