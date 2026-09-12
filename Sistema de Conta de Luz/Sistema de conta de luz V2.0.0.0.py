#Sistema de conta de luz
#Feito por Lucas Verissimo
#V2.0.0.0
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

def sistema_luz():

    for meses, meses_num in anus.items():
        print(f"- {meses.title()} mês {meses_num} -")
        print("-------------------------------------")

    
    while 0 < meses_num <= 12:
        try:
            meses_num = int(input("Insira o mês que o senhor quer saber a sua conta \n>  "))
            if meses_num == 1:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$130.00")
                input("Aperte Enter para voltar ao menu de meses \n>  ")
                sistema_luz()
                limpar_tela()
            
            elif meses_num == 2:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$130.00")
                input("Aperte Enter para voltar ao menu de meses \n>  ")
                sistema_luz()
                limpar_tela()
            
            elif meses_num == 3:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$120.00")
                input("Aperte Enter para voltar ao menu de meses \n>  ")
                sistema_luz()
                limpar_tela()
            
            elif meses_num == 4:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$110.00")
                input("Aperte Enter para voltar ao menu de meses \n>  ")
                sistema_luz()
                limpar_tela()
            
            elif meses_num == 5:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$100.00")
                input("Aperte Enter para voltar ao menu de meses \n>  ")
                sistema_luz()
                limpar_tela()
            
            elif meses_num == 6:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$95.00")
                input("Aperte Enter para voltar ao menu de meses \n>  ")
                sistema_luz()
                limpar_tela()
            
            elif meses_num == 7:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$95.00")
                input("Aperte Enter para voltar ao menu de meses \n>  ")
                sistema_luz()
                limpar_tela()
            
            elif meses_num == 8:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$100.00")
                input("Aperte Enter para voltar ao menu de meses \n>  ")
                sistema_luz()
                limpar_tela()
            
            elif meses_num == 9:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$110.00")
                input("Aperte Enter para voltar ao menu de meses \n>  ")
                sistema_luz()
                limpar_tela()
            
            elif meses_num == 10:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$115.00")
                input("Aperte Enter para voltar ao menu de meses \n>  ")
                sistema_luz()
                limpar_tela()
            
            elif meses_num == 11:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$120.00")
                input("Aperte Enter para voltar ao menu de meses \n>  ")
                sistema_luz()
                limpar_tela()
            
            elif meses_num == 12:
                print(f"O valor da luz gasto deste mês, {usuario}, é de R$125.00")
                input("Aperte Enter para voltar ao menu de meses \n>  ")
                sistema_luz()
                limpar_tela()
            
            else:
                print("Entrada inválida, Digite apenas números no intervalo de (1-12): ")
            
        except ValueError:
            print("\nError 404, Use apenas números inteiros seu animal .-.\n")
sistema_luz()

