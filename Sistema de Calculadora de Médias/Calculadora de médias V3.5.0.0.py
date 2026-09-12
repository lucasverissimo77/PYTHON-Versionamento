#Calculadora de média de notas
#Feito por Lucas do Vale Verissimo da Costa
#V2.0.0.0
import os
import time 


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()
time.sleep(0.1)



usuario = print("Qual seu nome?:")
input(">  ").strip().lower()

while True:
    print("\nOpção 1: Calcular média") 
    print("Opção 2: Somar notas")
    try:
        opcao = int(input(f"{usuario} Qual opção você quer escolher ? ")) 
        resposta = input(">  ").strip().lower()
        if opcao in (1, 2):
            break
        else:
            print("Por favor digite apenas '1' ou '2'")
    except ValueError:
        print("Entrada inválida, digite apenas números inteiros: ")
        resposta = input(">  ").strip().lower()


if opcao == 1 :
    def calcular_medias():
        medias = []

        while True:
            try:
                total_notas = int(print(f"{usuario} Quantas notas você deseja saber a sua média?: "))
                input(">  ").strip().lower()
                if total_notas > 0:
                    break
                print("Por Favor digite um número MAIOR que Zero.")
            except ValueError:
                print("Entrada inválida, digite apenas números inteiros: ")
                input(">  ").strip().lower()

        for i in range(1, total_notas +1):
            while True:
                try:
                    nota = float(input(f"Fale sua {i}º nota: "))

                    if 0<= nota <= 10:
                        medias.append(nota)
                        break
                    else:
                        print("Por Favor digite uma nota válida de 0 a 10")
                        input(">  ").strip().lower()
                except ValueError:
                    print("Entrada inválida, digite apenas números...")
                    input(">  ").strip().lower()

        print("\n   ---Notas digitadas---   ")
        for i in range(total_notas):
            print(f"O indíce {i} = {medias[i]}")

        media = sum(medias) / total_notas
        print(f"\nA sua média é {media:.2f}")
        if media >= 7:
            print(f"Você está Aprovado {usuario}")
        else:
            print(f"Você está reprovado {usuario}")
    calcular_medias()



elif opcao == 2:
    def somatorio_de_notas():

        notas = []

        while True:
            try:
                total_notas = int(input(f"{usuario} Quantas notas você deseja saber o seu somátório?: "))
                input(">  ").strip().lower()
                if total_notas > 0:
                    break
                print("Por Favor digite um número MAIOR que Zero.")
                input(">  ").strip().lower()
            except ValueError:
                print("Entrada inválida, digite apenas números inteiros: ")
                input(">  ").strip().lower()

        for i in range(1, total_notas +1):
            while True:
                try:
                    nota = float(input(f"Fale sua {i}º nota: "))
                    input(">  ").strip().lower()

                    if 0<= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Por Favor digite uma nota válida de 0 a 10")
                        input(">  ").strip().lower()

                except ValueError:
                    print("Entrada inválida, digite apenas números...")

        print("\n   ---Notas digitadas---   ")
        for i in range(total_notas):
            print(f"O indíce {i} = {notas[i]}")

        somatorio = sum(notas)
        print(f"\nO seu somatório é {somatorio:.2f}")
        if somatorio >= 15:
            print(f"Você está Aprovado {usuario}")
        else:
            print(f"Você está reprovado {usuario}")


    somatorio_de_notas()