# Problema 2 – Academia e Desempenho dos Atletas

# Lista de atletas
atletas = [
    {
        "nome": "Larissa",
        "idade": 22,
        "modalidades": ["Natação", "Corrida"],
        "treinos": {"Natação": 15, "Corrida": 10}
    },
    {
        "nome": "Rosa",
        "idade": 28,
        "modalidades": ["Futebol", "Corrida", "Musculação"],
        "treinos": {"Futebol": 20, "Corrida": 5, "Musculação": 12}
    },
    {
        "nome": "Flora",
        "idade": 19,
        "modalidades": ["Musculação", "Natação", "Yoga", "Corrida"],
        "treinos": {"Musculação": 8, "Natação": 10, "Yoga": 6, "Corrida": 3}
    }
]

#  média de idade dos atletas que praticam um esporte 
def media_idade(atletas, esporte):
    praticantes = [a["idade"] for a in atletas if esporte in a["modalidades"]]
    if praticantes:
        return sum(praticantes) / len(praticantes)
    else:
        return None

# esporte mais treinado de um atleta 
def esporte_mais_treinado(atletas, nome):
    for a in atletas:
        if a["nome"] == nome:
            if a["treinos"]:
                return max(a["treinos"], key=a["treinos"].get)
    return None

#  atletas com mais de 2 modalidades 
def atletas_multimodalidades(atletas):
    return [a["nome"] for a in atletas if len(a["modalidades"]) > 2]

print("Abaixo seguem os resultados:")

#  média de idade dos que praticam Natação
esporte = "Natação"
media = media_idade(atletas, esporte)
if media:
    print(f"Média de idade dos que praticam {esporte}: {media:.1f}")
else:
    print(f"Nenhum atleta pratica {esporte}.")

# esporte mais treinado de Bruno
nome = "Flora"
mais_treinado = esporte_mais_treinado(atletas, nome)
if mais_treinado:
    print(f"Esporte mais treinado de {nome}: {mais_treinado}")
else:
    print(f"Atleta {nome} não foi encontrado ou sem treinos.")

# lista de atletas com mais de 2 modalidades
lista_multimodalidades = atletas_multimodalidades(atletas)
print("Atletas com mais de 2 modalidades:", lista_multimodalidades)