# 5. Registro de Pontos em Jogos
# Contexto: Uma liga de esportes registra pontos de 3 times em 4 jogos.
# Tarefa: Crie uma matriz 3x4 com os pontos e determine qual time teve maior pontuação total.


pontos = []


for time in range(3):
    print(f"\nDigite os pontos do Time {time + 1} nos 4 jogos:")
    jogos = []
    for jogo in range(4):
        ponto = int(input(f"  Jogo {jogo + 1}: "))
        jogos.append(ponto)
    pontos.append(jogos)


totais = []
print("\nTotal de pontos por time:")
for i in range(3):
    total = sum(pontos[i])
    totais.append(total)
    print(f"  Time {i + 1}: {total} pontos")


maior_pontuacao = max(totais)
time_vencedor = totais.index(maior_pontuacao) + 1

print(f"\nTime com maior pontuação: Time {time_vencedor} ({maior_pontuacao} pontos)")