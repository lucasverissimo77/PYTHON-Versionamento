#Calculadora de média de notas
#Feito por Lucas do Vale Verissimo da Costa
#V2.0.0.0

def calcular_medias():
    medias = []


    while True:
        try:
            total_notas = int(input("Quantas notas você deseja saber a sua média?: "))
            if total_notas > 0:
                break
            print("Por Favor digite um número MAIOR que Zero.")
        except ValueError:
            print("Entrada inválida, digite apenas números inteiros: ")

    for i in range(1, total_notas +1):
        while True:
            try:
                nota = float(input(f"Fale sua {i}º nota: "))

                if 0<= nota <= 10:
                    medias.append(nota)
                    break
                else:
                    print("Por Favor digite uma nota válida de 0 a 10")

            except ValueError:
                print("Entrada inválida, digite apenas números...")

    print("\n   ---Notas digitadas---   ")
    for i in range(total_notas):
        print(f"O indíce {i} = {medias[i]}")

    media = sum(medias) / total_notas
    print(f"\nA sua média é {media:.2f}")

calcular_medias()
