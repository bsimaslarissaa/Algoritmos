# Caso3: Supermercado – Controle de Estoque
# Um supermercado mantém uma lista de produtos e seus preços.
# Cada item será representado como [nome, quantidade, preco_unitario].
# • O sistema deve:
# 1. Calcular o valor total em estoque.
# 2. Encontrar o produto de maior valor total (quantidade × preço).
# 3. Gerar uma lista apenas com os nomes dos produtos com estoque abaixo de 5
# unidades.
# 4. Permitir buscar um produto pelo nome e retornar seus dados.

produtos = [
    ["Arroz", 10, 6.0],
    ["Feijão", 3, 4.5],
    ["Carne", 7, 5.0],
    ["Farinha", 2, 6.5],
    ["Açúcar", 15, 4.0]
]

valor_total = sum(qtd * preco for _, qtd, preco in produtos)

maior_produto = max(produtos, key=lambda p: p[1] * p[2])

estoque_baixo = [nome for nome, qtd, _ in produtos if qtd < 5]

busca = input("Digite o nome do produto que deseja buscar: ").strip()
encontrado = None
for nome, qtd, preco in produtos:
    if nome.lower() == busca.lower():
        encontrado = [nome, qtd, preco]
        break

print("Resultados:")
print("Valor total em estoque: R$", valor_total)
print("Produto de maior valor total:", maior_produto[0],
      f"(R$ {maior_produto[1] * maior_produto[2]:.2f})")
print("Produtos com estoque baixo (<5):", estoque_baixo)

if encontrado:
    print(f"Produto encontrado: Nome={encontrado[0]}, "
          f"Quantidade={encontrado[1]}, Preço=R${encontrado[2]}")
else:
    print("Produto não encontrado.")