# 7. Vendas Semanais
# Contexto: Uma cafeteria registra vendas de 5 produtos durante 7 dias.
# Tarefa: Armazene os valores em uma matriz 5x7 e calcule a receita total semanal de cada produto.


vendas = []

for produto in range(5):
    print(f"\nDigite as vendas diárias do Produto {produto + 1}:")
    vendas_produto = []
    for dia in range(7):
        valor = float(input(f"  Dia {dia + 1}: "))
        vendas_produto.append(valor)
    vendas.append(vendas_produto)

print("\nReceita total semanal de cada produto:")
for i in range(5):
    total_semanal = sum(vendas[i])
    print(f"  Produto {i + 1}: R$ {total_semanal:.2f}")