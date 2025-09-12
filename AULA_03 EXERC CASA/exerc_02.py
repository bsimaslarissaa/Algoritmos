# Caso6: Sistema de Biblioteca


livros = [
    ["Dom Casmurro", "Ana", 5],
    ["1984", "Carlos", 12],
    ["O Hobbit", "Marina", 3],
    ["A Revolução dos Bichos", "João", 15],
    ["Memórias Póstumas de Brás Cubas", "Luiza", 8]
]


sistema_biblioteca = {
    "livros_maior_7dias": [livro for livro in livros if livro[2] > 7],
    "livro_mais_tempo": max(livros, key=lambda x: x[2]),
    "usuarios_com_livros": [livro[1] for livro in livros],
    "media_dias": sum(livro[2] for livro in livros) / len(livros)
}


print("Sistema de Biblioteca")
print("\n1. Livros emprestados há mais de 7 dias:")
for l in sistema_biblioteca["livros_maior_7dias"]:
    print(f" - {l[0]} (Usuário: {l[1]}, {l[2]} dias)")

print(f"\n2. Livro emprestado há mais tempo: {sistema_biblioteca['livro_mais_tempo'][0]} "
      f"({sistema_biblioteca['livro_mais_tempo'][2]} dias, Usuário: {sistema_biblioteca['livro_mais_tempo'][1]})")

print(f"\n3. Usuários com livros emprestados: {sistema_biblioteca['usuarios_com_livros']}")

print(f"\n4. Média de dias de empréstimo: {sistema_biblioteca['media_dias']:.2f}")