#Fila de Pacientes
#Versão 1.0
#Feito por Lucas do Vale

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()




lista = []

# Programa para ordenar nomes em ordem alfabética usando Bubble Sort

def bubble_sort(lista):
    """
    Ordena a lista usando o algoritmo Bubble Sort.
    Funciona para strings e ignora diferenças de maiúsculas/minúsculas.
    """
    n = len(lista)
    for i in range(n):
        for j in range(n - 1):
            # Comparação ignorando maiúsculas/minúsculas
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j +1]
                lista[j +1] = aux
    return lista

def main():
    print("Quantas pessoas você deseja inserir neste programa?")
    quantidade = int(input(">  "))

    for quantidade_de_pessoas in range (1, quantidade  + 1):
        try:
            entrada = input("Digite os nomes separados por virgula \n>  ").strip()
            if not entrada:
                print("Nenhum nome foi encrontrado")
                return
            
            lista.append(entrada)

            if not entrada:
                print("Lista de nomes vazia")
                return

    
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        
    nomes_ordenados = bubble_sort(lista)
    print("\nNomes em ordem alfabética! ")
    print(lista)
main()
