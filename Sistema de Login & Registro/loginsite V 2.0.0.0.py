#versão 2.0.0.0 em python
#Feito por Lucas Dell Vale Verissimo

import os #biblioteca para interagir com o sistema operacional
import time

usuarios_cadastrados = {
    "lucas": "lucas777",
    "adm_joao batista": "777adm"
}


def limpar_tela ():
    #Limpa o terminal antes de começar para evitar problemas...
    os.system('cls' if os.name == 'nt' else 'clear')

#Inicializa o terminal limpando qualquer comando fantasma
limpar_tela()
time.sleep(0.1) #Aguarda 100milissegundos para a máquina terminar de processar


while True:
    print("\n" + "="*40)
    print("Sistema de acesso")
    print("="*40)
    print("Você já faz parte de nosso site? (Sim/Nao) ou digite 'sair': ")
    resposta = input("> ").strip().lower()


    #Caso a pessoa queira sair
    if response := resposta == "sair":
        print("Até logo!!")
        break

    #Validação da resposta:
    while resposta != "sim" and resposta != "nao":
        print("Resposta inválida! Tente novamente (Sim/Nao) ou 'sair': ")
        resposta = input("> ").strip().lower()
        if resposta == "sair":
            break


        if resposta == "sair":
            print("Até logo!!")
            break
        

    #Caso a pessoa não tenha cadastro
    if resposta == "nao":
        print("\n--- Tela de Cadastro ---")
        print("Digite seu nome de Usúario: ")
        usuario = input("> ").strip().lower()

        #Verificar se o nome já existe no sistema...
        while usuario in usuarios_cadastrados:
            print("Usúario já existente, escolha outro nome de usúario!")
            usuario = input("> ").strip().lower()

        cadastro_valido = False
        while not cadastro_valido:
            senha = input("Digite sua senha: ")
            senha_salva = input("Confirme sua senha: ")

            if senha == senha_salva:
                #Salva o Usúario em um banco de dados
                usuarios_cadastrados[usuario] = senha
                print(f"\nOla, {usuario}! Você se cadastrou com sucesso!")
                print("Agora Você já pode fazer login no sistema.")
                cadastro_valido = True
            else:
                print("Senhas diferentes! Tente cadastrar a senha novamente. \n")

    #Caso a pessoa já tenha login ou conta ativa...
    elif resposta == "sim":
        print("\n --- Tela de Login ---")
        print("Digite seu nome de Usúario: ")
        usuario_salvo = input("> ").strip().lower()

        #Verifica se o usúario existe e define a senha correta
        if usuario_salvo not in usuarios_cadastrados:
            print("Usúario inexistente!")
        else:
            #Define a senha de acordo com o usúario escolhido!
            senha_salva = usuarios_cadastrados[usuario_salvo]

            senha = input("Digite sua senha: ")

            #Contador de tentativas para caso o usúario erre a senha 3 vezes ele seja bloqueado...
            tentativas = 3
            while senha != senha_salva and tentativas > 1:
                tentativas -= 1
                print(f"Senhas incorreta! Você tem mais {tentativas} de chance(s).")
                senha = input("Digite sua senha novamente: ")

            ##Verificação final do acesso...
            if senha == senha_salva:
                print(f"Acesso concedido!! Bem-Vindo ao nosso site, {usuario_salvo}.")
                time.sleep(1)

                #Redirecionando um administrador em um painel especial para admins
                if usuario_salvo == "adm_joao batista":
                    #programa de admin
                    limpar_tela()
                    print("\n" + "#"*40)
                    print("         Painel de administrador         ")
                    print("#"*40)
                    print(f"Bem-Vindo, supremo ADMIN {usuario_salvo}!")
                    print("\n[1] Ver todos os usúarios cadastrados")
                    print("[2] Deletar um usúario do sistema")
                    print("[3] Deslogar e voltar ao menu principal")

                    opcao_adm = input("\nEscolha uma opção de admin: ")
                    if opcao_adm == "1":
                        print("\n--- Lista de Usúarios no sistema ---")
                        for user in usuarios_cadastrados:
                            print(f"- {user}")
                            print("\nPressione ENTER para sair do Painel de ADMIN")
                            input()
                        else:
                            print("\nSaindo do painel Administrativo...")
                            time.sleep(1)
                    else:
                        #Programa de usúario normal
                        print("\n--- Área do Usúario ---")
                        print("Você está no painel comum. Aproveite o conteúdo do site...")
                        print("\nPressione Enter para deslogar e voltar para o menu")
                        input()

                else:
                    print("\nSenha incorreta! Você tem mais 0 chance(s).")
                    print("\nAcesso Bloqueado! Número de tentativas excedido!!")
                    print("\nPressione Enter para desligar e voltar ao menu...")
                    input()
