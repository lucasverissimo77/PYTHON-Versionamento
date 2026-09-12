#Sistema de Controle de Temperatura
#Feito por Lucas Verissimo
#Versão 2.0.0.0

import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')



def main():
    limpar_tela()
    soma = 0
    dia_maior = 0
    maior_temp = float('-inf')
    menor_temp = float('inf')
    acima_30graus = 0
    print("\n>>>Sistema de Controle De Temperatura<<<\n")
    for dia in range(1,8):
        temperatura = float(input(f"Digite a temperatura do {dia}º dia: \n>  "))
        soma += temperatura
        if temperatura > maior_temp:
            maior_temp = temperatura
            dia_maior = dia

        elif temperatura < menor_temp:
            menor_temp = temperatura

        elif temperatura > 30:
            acima_30graus += 1

    media = soma / 7

    print(">>>Resultados<<<")
    print(f"Temperatura média de {media:.2f}º Graus")
    print(f"Maior Temperatura: {maior_temp:.1f} Cº (Dia {dia_maior})")
    print(f"Menor Temperatura: {menor_temp:.1f} Cº")
    print(f"Dias com temperatura maior de 30 Cº: {acima_30graus}")
main()