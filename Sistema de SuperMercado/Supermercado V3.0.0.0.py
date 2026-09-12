# Supermercado
# Feito por Lucas do Vale Verissimo
# V3.0.0.0
catalogo = {
    "banana" : 4.50,            "maçã" : 10.00,
    "coca cola" : 8.00,         "guaraná" : 7.00,
    "prudence" : 12.00,         "Salgado" : 10.00,
    "chocolate" : 6.00,         "presente misterioso" : 20.00,
    "pepsi" : 7.00,             "pão" : 5.00,
    "programa lixo" : 100.00,   "bolo" : 70.00,
    "Biscoito" : 5.00,          "Docinho" : 100.00,
}
preco_obtido = 100.00
usuario_adm = "lucas"

def supermercado():
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
                
                quantidade = int(input(f"{usuario} Quantos itens deseja comprar? \nOu digite (0) Para sair do sistema. \n> "))
                valor_total = 0

                if quantidade == 0:
                    print("Até logo!!")
                    break
                elif quantidade > 0:
                    for i in range(quantidade):
                        escolha = input(f"Escolha o item {i+1}: \n> ").strip().lower()
                        if escolha in catalogo:
                            preco_unitario = catalogo[escolha]
                            valor_total += preco_unitario
                            print(f"{escolha.title()} adicionado! valor: R${preco_unitario:.2f} ")
                        else:
                            print("Produto não encontrado no catálogo")
                    print(f"\nCompra finalizada! Valor total: R${valor_total:.2f}")
                    break
                else:
                    print("Por favor, digite um número maior ou igual a um ou (0) para sair!")

            # CASO A PESSOA RESPONDA NAO
            elif resposta_inicial == "nao":
                usuario_salvo = input("Digite seu nome de usúario: \n>  ")
                if usuario_salvo != "lucas".strip().lower():
                    print(f"Seja bem vindo {usuario_salvo} Você já pode logar em nosso mercado!")
                    supermercado()
                else:
                    print("Este usúario já existe.")
                    print("Tente novamente.")
                    supermercado()

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
                        supermercado()
                else:
                    print("Saia daqui imediatamente! Credenciais incorretas.")
                    break

        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros onde for solicitado.")
supermercado()