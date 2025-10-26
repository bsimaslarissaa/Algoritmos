# 2. Grade de Notas de Alunos
# Contexto: Uma turma de 4 alunos realizou 3 provas.
# Tarefa: Armazene as notas em uma matriz 4x3 e calcule a média de cada aluno e a média de cada prova.

notas = []

for aluno in range(4):
    print(f"\nDigite as 3 notas do Aluno {aluno + 1}:")
    notas_aluno = []
    for prova in range(3):
        nota = float(input(f"  Nota da Prova {prova + 1}: "))
        notas_aluno.append(nota)
    notas.append(notas_aluno)

print("\nMédia de cada aluno:")
for i in range(4):
    media_aluno = sum(notas[i]) / 3
    print(f"  Aluno {i + 1}: {media_aluno:.2f}")

print("\nMédia de cada prova:")
for j in range(3):
    soma = 0
    for i in range(4):
        soma += notas[i][j]
    media_prova = soma / 4
    print(f"  Prova {j + 1}: {media_prova:.2f}")