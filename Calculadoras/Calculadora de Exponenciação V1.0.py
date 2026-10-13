#Calculadora de Exponenciação
#Versão 1.0
#Feito Por: Lucas Verissimo

import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()

def calcular(base, expoente):
    if expoente == 0 or base == 1:
        return 1
    else:
        return base * calcular(base, expoente - 1)
    
def main():
    print("=" * 60)
    print("Seja Bem vindo a nossa calculadora de expoentes com recursividade")
    print("=" * 60)
    numero = int(input("Insira o número da base \n>  "))
    exp = int(input("Insira o número do expoente \n>  "))
    print("Carregando...")
    time.sleep(.5)
    limpar_tela()
    resultado = calcular(numero, exp)
    print(f"O resultado de {numero} elevado a {exp} é: {resultado}")
main()