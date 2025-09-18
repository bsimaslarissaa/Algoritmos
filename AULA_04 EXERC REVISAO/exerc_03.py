# Problema 3 – Loja de Música Online com Estatísticas

musicas = [
    {
        "titulo": "Quando a chuva Passar",
        "artista": "Sandy e Junior",
        "downloads": 1200,
        "avaliacoes": [5, 4, 4, 5, 5]
    },
    {
        "titulo": "Fica Tudo Bem",
        "artista": "Silva",
        "downloads": 2500,
        "avaliacoes": [4, 4, 3, 5, 4, 5]
    },
    {
        "titulo": "Palavras no Corpo",
        "artista": "Gal Costa",
        "downloads": 1800,
        "avaliacoes": [3, 4, 4, 2, 5]
    },
    {
        "titulo": "Sozinho",
        "artista": "Caetano Veloso",
        "downloads": 3000,
        "avaliacoes": [5, 5, 5, 4, 5]
    }
]

# calcular média de avaliação de cada música 
def calcular_media_avaliacoes(musicas):
    medias = {}
    for m in musicas:
        if m["avaliacoes"]:
            media = sum(m["avaliacoes"]) / len(m["avaliacoes"])
            medias[m["titulo"]] = media
        else:
            medias[m["titulo"]] = 0
    return medias

# artista com maior número total de downloads 
def artista_mais_downloads(musicas):
    downloads_por_artista = {}
    for m in musicas:
        artista = m["artista"]
        downloads_por_artista[artista] = downloads_por_artista.get(artista, 0) + m["downloads"]
    return max(downloads_por_artista, key=downloads_por_artista.get)

#  ranking das músicas mais bem avaliadas
def ranking_musicas(musicas):
    medias = calcular_media_avaliacoes(musicas)
    return sorted(medias.items(), key=lambda x: x[1], reverse=True)


print("ABAIXO SEGUEM OS RESULTADOS:")

# Médias das músicas
print("\nMédias de avaliação das músicas:")
for titulo, media in calcular_media_avaliacoes(musicas).items():
    print(f"{titulo}: {media:.2f}")

#  Artista com mais downloads
print("\nArtista com maior número de downloads:")
print(artista_mais_downloads(musicas))

# Ranking das músicas
print("\nRanking das músicas mais bem avaliadas:")
for pos, (titulo, media) in enumerate(ranking_musicas(musicas), start=1):
    print(f"{pos}. {titulo} - {media:.2f}")