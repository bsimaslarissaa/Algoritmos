# 09 Ler um arquivo CSV e retornar os dados como lista de dicionários.

import csv

caminho_csv = r"C:\Users\larissa.simas\Documents\lista\frutas.csv"

try:
    lista_dados = []

    with open(caminho_csv, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            lista_dados.append(dict(linha))

    print(lista_dados)

except FileNotFoundError:
    print("Erro: Arquivo CSV não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")