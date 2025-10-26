# 8. Distribuição de Cadeiras
# Contexto: Uma sala de cinema tem 5 filas com 6 cadeiras cada.
# Tarefa: Crie uma matriz 5x6 e marque quais cadeiras estão ocupadas com “X” e quais estão livres com “O”

cadeiras = [["O" for _ in range(6)] for _ in range(5)]

print("Informe as cadeiras ocupadas. Para terminar, digite -1 para a fila.")

while True:
    fila = int(input("Digite o número da fila (1 a 5) ou -1 para sair: "))
    if fila == -1:
        break
    if fila < 1 or fila > 5:
        print("Fila inválida! Tente novamente.")
        continue

    cadeira = int(input("Digite o número da cadeira (1 a 6): "))
    if cadeira < 1 or cadeira > 6:
        print("Cadeira inválida! Tente novamente.")
        continue

    cadeiras[fila - 1][cadeira - 1] = "X"
    print(f"Cadeira {cadeira} da fila {fila} marcada como ocupada.")

print("\nMapa de cadeiras (X = ocupada, O = livre):")
for i, fila in enumerate(cadeiras, start=1):
    print(f"Fila {i}: {' '.join(fila)}")