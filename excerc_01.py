# Crie um programa que: Receba as temperaturas de 7 dias e armazene em uma lista. 
# Mostre a média das temperaturas da semana.Informe o dia mais quente e o dia mais frio.
# Mostre quantos dias ficaram acima da média.

def analisar_temperaturas():
    temperaturas = []

    for i in range(7):
        temp = float(input(f"Digite a temperatura do dia {i + 1}: "))
        temperaturas.append(temp)

    media = sum(temperaturas) / len(temperaturas)
    print(f"\nA média das temperaturas da semana foi: {media:.2f}°C")


    dia_quente = temperaturas.index(max(temperaturas)) + 1
    dia_frio = temperaturas.index(min(temperaturas)) + 1
    print(f"O dia mais quente foi o dia {dia_quente} com {max(temperaturas):.2f}°C")
    print(f"O dia mais frio foi o dia {dia_frio} com {min(temperaturas):.2f}°C")

    dias_acima_media = sum(1 for temp in temperaturas if temp > media)
    print(f"\nHouve {dias_acima_media} dias com temperatura acima da média.")



analisar_temperaturas()