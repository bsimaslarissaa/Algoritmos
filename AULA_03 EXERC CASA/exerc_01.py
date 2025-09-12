# Caso4: Análise de Vendas Mensais

# Lista de vendas por dia do mês
vendas = [10, 15, 20, 5, 0, 8, 25, 18, 30, 12, 7, 14]


analise_vendas = {
    "total": sum(vendas),
    "dia_max": vendas.index(max(vendas)) + 1,   
    "dia_min": vendas.index(min(vendas)) + 1,
    "media": sum(vendas) / len(vendas),
    "dias_acima_media": []
}


analise_vendas["dias_acima_media"] = [
    i+1 for i, v in enumerate(vendas) if v > analise_vendas["media"]
]


print("Análise de Vendas Mensais:")
print(f"Total de vendas no mês: {analise_vendas['total']}")
print(f"Dia com mais vendas: Dia {analise_vendas['dia_max']} ({max(vendas)} vendas)")
print(f"Dia com menos vendas: Dia {analise_vendas['dia_min']} ({min(vendas)} vendas)")
print(f"Média de vendas por dia: {analise_vendas['media']:.2f}")
print(f"Dias acima da média: {analise_vendas['dias_acima_media']}")