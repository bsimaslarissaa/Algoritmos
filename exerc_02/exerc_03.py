# Questao 3- Leia as notas de uma turma e Calcule a média; Mostre a maior e a menor nota; Exiba o percentual de alunos acima da média.

notas = []

qtd = int(input("Quantos alunos na turma? "))

for i in range(qtd):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / qtd

maior = max(notas)
menor = min(notas)

acima_media = sum(1 for nota in notas if nota > media)
percentual = (acima_media / qtd) * 100

print("\n--- Resultados ---")
print(f"Média da turma = {media:.2f}")
print(f"Maior nota = {maior}")
print(f"Menor nota = {menor}")
print(f"Percentual de alunos acima da média = {percentual:.2f}%")