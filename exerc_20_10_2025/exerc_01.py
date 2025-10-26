# 1. Controle de Temperatura de Salas
# Contexto: Uma empresa monitora a temperatura de 5 salas, 3 vezes ao dia.
# Tarefa: Armazene as temperaturas em uma matriz 5x3. Calcule a temperatura media de cada sala.

temperaturas = []

for sala in range(5):
    print(f"\nInforme as 3 temperaturas da Sala {sala + 1}:")
    temp_sala = []
    for leitura in range(3):
        temp = float(input(f"  Temperatura {leitura + 1}: "))
        temp_sala.append(temp)
    temperaturas.append(temp_sala)

print("\nMédias das temperaturas por sala:")
for i in range(5):
    media = sum(temperaturas[i]) / 3
    print(f"  Sala {i + 1}: {media:.2f} °C")