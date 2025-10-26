# Contexto: Uma academia planeja 3 tipos de exercícios para 4 alunos diferentes.
# Tarefa: Crie uma matriz 4x3 que registre quantas repetições cada aluno deve fazer e calcule o total de repetições de cada exercício

repeticoes = []

for aluno in range(4):
    print(f"\nDigite as repetições dos 3 exercícios para o Aluno {aluno + 1}:")
    rep_aluno = []
    for exercicio in range(3):
        rep = int(input(f"  Exercício {exercicio + 1}: "))
        rep_aluno.append(rep)
    repeticoes.append(rep_aluno)


print("\nTotal de repetições por exercício:")
for exercicio in range(3):
    total = sum(repeticoes[aluno][exercicio] for aluno in range(4))
    print(f"  Exercício {exercicio + 1}: {total} repetições")