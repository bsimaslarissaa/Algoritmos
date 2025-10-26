# 10. Registro de Chuva
# Contexto: Uma estação meteorológica registra chuva em 7 dias, para 3 cidades.
# Tarefa: Crie uma matriz 3x7 com os valores de chuva (mm) e determine qual cidade teve mais chuva na semana.

chuva = []

for cidade in range(3):
    print(f"\nDigite a quantidade de chuva (mm) para a Cidade {cidade + 1} em 7 dias:")
    chuva_cidade = []
    for dia in range(7):
        valor = float(input(f"  Dia {dia + 1}: "))
        chuva_cidade.append(valor)
    chuva.append(chuva_cidade)

totais = []
for i in range(3):
    total = sum(chuva[i])
    totais.append(total)
    print(f"Cidade {i + 1} - Total de chuva na semana: {total:.2f} mm")

max_chuva = max(totais)
cidade_mais_chuva = totais.index(max_chuva) + 1

print(f"\nCidade com mais chuva na semana: Cidade {cidade_mais_chuva} ({max_chuva:.2f} mm)")