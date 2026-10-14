#Sistema de Calculadora de Fatoração com e sem recursão
#Feito por Lucas Verissimo
#Versão 1.0

import time
import os

resposta_sim = ["sim", "s", "si", "sm"]
resposta_nao = ["nao", "não", "n", "na", "nã", "no"]


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def fatorial_recursao(numero):
    inicio = time.time()
    if numero == 0 or numero == 1:
        return 1
    print("Conta realizada com Sucesso!")
    fim = time.time()
    tempo_execucao = fim - inicio
    print(f"O tempo de execução foi {tempo_execucao:.6f} segundos")
    return numero * fatorial_recursao(numero - 1)
    
    
def fatorial_repeticao(numero):
    res = 1
    for i in range(1, numero + 1):
        res = res * i
    print("Conta realizada com Sucesso!")    
    return f'O resultado da conta foi: {res}'


def main():
    limpar_tela()
    print("=" * 45)
    print("Sistema de Calculadora Fatorial")
    print("Sem Recursão")
    print("=" * 45)
    print("Bom dia Senhor! Insira o numero que será fatorado")
    numero = int(input(">  ").strip())
    inicio_repeticao = time.time()
    saida = fatorial_repeticao(numero)
    fim_repeticao = time.time()
    print(f"Resposta é: \n>  {saida}")
    input("Aperte Enter para continuar")
    limpar_tela()
    print("Você quer executar o mesmo programa com recursão?")
    resposta_usuario = input(">  ").lower()
    if resposta_usuario in resposta_sim:
        print("Executando o novo sistema, aguarde...")
        time.sleep(2)
        limpar_tela()
        print("=" * 45)
        print("Sistema de Calculadora Fatorial")
        print("Sem Recursão")
        print("=" * 45)
        print("Digite o numero que será fatorado")
        numero = int(input(">  ").strip())
        inicio_recursao = time.time()
        saida = fatorial_recursao(numero)
        fim_recursao = time.time()
        print(f"A resposta é: \n>  {saida}")
        tempo_execucao_recursao = fim_recursao - inicio_recursao
        print(f"O tempo de Execução do Sistema de repetição foi de {tempo_execucao_repeticao} segundos")
        print(f"O tempo de Execução do Sistema de Repetição foi de {tempo_execucao_recursao} segundos")
        print("Digite Enter para sair")
        input(">  ")
    elif resposta_usuario in resposta_nao:
        limpar_tela()
        tempo_execucao_repeticao = fim_repeticao - inicio_repeticao
        print(f"O tempo de Execução do Sistema de repetição foi de {tempo_execucao_repeticao} segundos")
        print("Digite Enter para sair")
        input(">  ") 
main()

