#Supermercado
#Feito por Lucas do Vale Verissimo
#V1.0.0.0

precos = 10.00
produtos = "banana", "prudence", "chocolate", "coca cola", "pepsi", "programa_lixo"
preco_obtido = 1000.00
while True:
    print("Seja Bem-Vindo a nossa loja online o senhor já faz parte de nosso sistema?")
    resposta_inicial = input(">  ").strip().lower()
    while resposta_inicial != "sim" and resposta_inicial != "nao":
        print("Resposta inválida digite apenas Sim/Não")
        resposta_inicial = input(">  ").strip().lower()

    if resposta_inicial == "sim":
        usuario = input("Qual seu nome de usúario?: \n>  ")
        if usuario == "lucas":
            print("Seja bem-vindo dono do mercado, meu herói, meu dono, meu criador...")
            print("O que o senhor quer fazer hoje?")
            print("Opção1: Ver produtos criados")
            print("Opção2: ver dinheiro arrecadado")
            print("Opção3: ver o nome do seu negócio")
            print("Opção4: Sair")
            opcao_adm = input("\nEscolha uma opção... \n>  ")
            if opcao_adm in (1, 2, 3, 4):
                break
            else:
                print("Por favor digite apenas os números da opção")
            if opcao_adm == "1":
                print(produtos)
            elif opcao_adm == "2":
                print(preco_obtido)
            elif opcao_adm == "3":
                print("Del Valle Company    ---     Quem é tu rapa que não sabe o nome da empresa, to de olho ein!!")
            elif opcao_adm == "4":
                print("Já vai meu mestre?")
                break