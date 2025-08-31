# Caso1: Controle de Presença em Sala de Aula
# Uma professora precisa registrar a presença dos alunos durante a semana.
# • Cada dia da semana terá uma lista com os nomes dos presentes.
# No final, ela precisa:
# 1. Saber quais alunos estiveram presentes todos os dias.
# 2. Saber quais alunos faltaram em pelo menos um dia.
# 3. Saber o número total de presenças por aluno.]

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
semana = []

for dia in dias:
    presentes = input(f"Digite os nomes dos alunos presentes na {dia}: ")

    lista_presentes = [nome.strip() for nome in presentes.split(",") if nome.strip() != ""]
    semana.append(lista_presentes)


todos_alunos = []
for dia in semana:
    for aluno in dia:
        if aluno not in todos_alunos:
            todos_alunos.append(aluno)


presentes_todos_dias = []
for aluno in todos_alunos:
    if all(aluno in dia for dia in semana):
        presentes_todos_dias.append(aluno)


faltaram_algum_dia = []
for aluno in todos_alunos:
    if aluno not in presentes_todos_dias:
        faltaram_algum_dia.append(aluno)


presencas = {}
for aluno in todos_alunos:
    presencas[aluno] = 0
    for dia in semana:
        if aluno in dia:
            presencas[aluno] += 1


print("Presentes todos os dias:", presentes_todos_dias)
print("Faltaram pelo menos um dia:", faltaram_algum_dia)
print("Número total de presenças por aluno:")
for aluno, qtd in presencas.items():
    print(f" - {aluno}: {qtd}")