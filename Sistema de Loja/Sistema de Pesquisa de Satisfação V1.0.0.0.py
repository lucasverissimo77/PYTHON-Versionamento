#Sistema de Pesquisa de Satisfação
#Feito Por Lucas Verissimo
#Versão 1.0.0.0

import os
import time
from collections import Counter

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)


participantes = 0

def pesquisa():
    limpar_tela()
    print("\n---Sistema de Pesquisa de Satisfação---\n")
    lista_notas = []
    total_notas = 0
    
    while True:
        try:
            print("Digite a sua nota: ")
            print("--> 0 Para Encerrar o sistema <--")
            nota = float(input(">  "))
            if nota != 0:
                lista_notas.append(nota)
                total_notas += 1
            elif nota == 0:
                print("Finalizando o Sistema e carregando dados")
                time.sleep(3.5)
                media = sum(lista_notas) / total_notas
                contagem = Counter(lista_notas)
                nota_mais_comum = contagem.most_common(1)[0]
                print(f"A quantidade de notas foram de {total_notas}")
                print(f"A sua média de notas é: {media:.2f}")
                print(f"A nota mais inserida foi {nota_mais_comum[0]} com {nota_mais_comum[1]} Ocorrencias")
                break
        except ValueError:
            print("Valor inserido não é Válido! ")
pesquisa()