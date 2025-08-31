# Caso2: Distâncias em Km
# 1. Receba as distâncias percorridas em 6 viagens e armazene em uma lista.
# 2. Calcule a distância total percorrida.
# 3. Mostre a maior e a menor distância.
# 4. Calcule a média das distâncias arredondada para cima (use math.ceil).

import math

distancias = []

for i in range(6):
    d = float(input(f"Digite a distância da viagem {i+1}: "))
    distancias.append(d)

total = sum(distancias)

maior = max(distancias)
menor = min(distancias)

media = math.ceil(total / len(distancias))

print("Resultados:")
print("Distâncias registradas:", distancias)
print("Distância total:", total)
print("Maior distância:", maior)
print("Menor distância:", menor)
print("Média arredondada para cima:", media)