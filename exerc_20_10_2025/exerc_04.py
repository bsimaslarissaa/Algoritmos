# 4. Controle de Estoque
# Contexto: Uma loja possui 4 produtos e verifica o estoque em 3 lojas diferentes.
# Tarefa: Crie uma matriz 4x3 com as quantidades de cada produto em cada loja e calcule o total de cada produto.

estoque = []


for produto in range(4):
    print(f"\nProduto {produto + 1}:")
    quantidades = []
    for loja in range(3):
        quantidade = int(input(f"  Quantidade na Loja {loja + 1}: "))
        quantidades.append(quantidade)
    estoque.append(quantidades)

print("\nTotal de cada produto em todas as lojas:")
for i in range(4):
    total = sum(estoque[i])
    print(f"  Produto {i + 1}: {total} unidades")