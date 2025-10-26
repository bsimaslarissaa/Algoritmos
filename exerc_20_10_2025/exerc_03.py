# 3. Agenda Semanal
# Contexto: Um consultório possui 5 dias de atendimento e 3 horários por dia.
#Tarefa: Armazene os nomes dos pacientes em uma matriz 5x3 e exiba a agenda completa.

agenda = []

for dia in range(5):
    print(f"\nDia {dia + 1}:")
    horarios = []
    for hora in range(3):
        nome = input(f"  Nome do paciente para o horário {hora + 1}: ")
        horarios.append(nome)
    agenda.append(horarios)

print("\nAgenda completa da semana:")
for dia in range(5):
    print(f"\nDia {dia + 1}:")
    for hora in range(3):
        print(f"  Horário {hora + 1}: {agenda[dia][hora]}")