# Problema 4 – Ranking de Filmes
# Lista de filmes de exemplo
filmes = [
    {
        "titulo": "Up Altas Aventuras",
        "diretor": "Larissa Simas",
        "bilheteria": 950,
        "avaliacoes": [9, 8, 10, 9, 8]
    },
    {
        "titulo": "Divertidamente",
        "diretor": "Marcos Tavares",
        "bilheteria": 500,
        "avaliacoes": [7, 8, 7, 9, 6]
    },
    {
        "titulo": "Como treinar seu Dragão",
        "diretor": "Orlando Gouveia",
        "bilheteria": 1200,
        "avaliacoes": [9, 9, 8, 10, 9]
    },
    {
        "titulo": "Comédia do Ano",
        "diretor": "João Silva",
        "bilheteria": 300,
        "avaliacoes": [6, 7, 7, 8, 6]
    },
    {
        "titulo": "Drama Épico",
        "diretor": "Ana Souza",
        "bilheteria": 800,
        "avaliacoes": [10, 9, 10, 8, 9]
    }
]

#  Top 3 maiores bilheterias 
def top_bilheteria(filmes):
    return sorted(filmes, key=lambda x: x["bilheteria"], reverse=True)[:3]

# Top 3 melhores avaliados 
def top_avaliacao(filmes):
    def media(f):
        return sum(f["avaliacoes"]) / len(f["avaliacoes"]) if f["avaliacoes"] else 0
    return sorted(filmes, key=media, reverse=True)[:3]

# Bilheteria por diretor 
def bilheteria_por_diretor(filmes):
    resultado = {}
    for f in filmes:
        diretor = f["diretor"]
        resultado[diretor] = resultado.get(diretor, 0) + f["bilheteria"]
    return resultado

#  Campeão de bilheteria por avaliação
def campeao(filmes):
    melhor = None
    melhor_score = -1
    for f in filmes:
        media = sum(f["avaliacoes"]) / len(f["avaliacoes"]) if f["avaliacoes"] else 0
        score = f["bilheteria"] * media  # combinação bilheteria * média
        if score > melhor_score:
            melhor_score = score
            melhor = f
    return melhor


print("Resultados\n")

print("Top 3 maiores bilheterias:")
for f in top_bilheteria(filmes):
    print(f"{f['titulo']} - {f['bilheteria']} milhões")

print("\nTop 3 melhores avaliados:")
for f in top_avaliacao(filmes):
    media = sum(f["avaliacoes"]) / len(f["avaliacoes"])
    print(f"{f['titulo']} - média {media:.2f}")

print("\nBilheteria por diretor:")
for diretor, total in bilheteria_por_diretor(filmes).items():
    print(f"{diretor}: {total} milhões")

print("\nCampeão absoluto:")
campeao_filme = campeao(filmes)
media = sum(campeao_filme["avaliacoes"]) / len(campeao_filme["avaliacoes"])
print(f"{campeao_filme['titulo']} (bilheteria {campeao_filme['bilheteria']} milhões, média {media:.2f})")

