# Caso5: Controle de Participação em um Evento

palestra = input("Digite os participantes da Palestra (separados por vírgula): ").split(",")
workshop = input("Digite os participantes do Workshop (separados por vírgula): ").split(",")
mesa_redonda = input("Digite os participantes da Mesa-redonda (separados por vírgula): ").split(",")

palestra = [n.strip() for n in palestra if n.strip()]
workshop = [n.strip() for n in workshop if n.strip()]
mesa_redonda = [n.strip() for n in mesa_redonda if n.strip()]

atividades = [palestra, workshop, mesa_redonda]

todos = []
for nome in palestra:
    if all(nome in atividade for atividade in atividades):
        todos.append(nome)

apenas_um = []
for atividade in atividades:
    for nome in atividade:
        contagem = sum(nome in a for a in atividades)
        if contagem == 1 and nome not in apenas_um:
            apenas_um.append(nome)

unicos = []
for atividade in atividades:
    for nome in atividade:
        if nome not in unicos:
            unicos.append(nome)

qtd_distintos = len(unicos)

print("Resultados:")
print("Participaram de todas as atividades:", todos)
print("Participaram de apenas uma atividade:", apenas_um)
print("Lista de todos os participantes:", unicos)
print("Número de participantes distintos:", qtd_distintos)