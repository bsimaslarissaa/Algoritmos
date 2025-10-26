# 6. Horários de Transporte
# Contexto: Um ponto de ônibus tem 4 linhas, cada uma com 3 horários.
# Tarefa: Armazene os horários em uma matriz 4x3 e permita que o usuário consulte os horários de uma linha específica


horarios = []

for linha in range(4):
    print(f"\nDigite os 3 horários da Linha {linha + 1}:")
    horarios_linha = []
    for h in range(3):
        horario = input(f"  Horário {h + 1}: ")
        horarios_linha.append(horario)
    horarios.append(horarios_linha)

linha_consulta = int(input("\nDigite o número da linha que deseja consultar (1-4): "))

if 1 <= linha_consulta <= 4:
    print(f"\nHorários da Linha {linha_consulta}:")
    for i, horario in enumerate(horarios[linha_consulta - 1], start=1):
        print(f"  Horário {i}: {horario}")
else:
    print("Linha inválida. Por favor, digite um número entre 1 e 4.")