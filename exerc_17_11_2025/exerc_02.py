# 02 Ler um arquivo linha por linha.

# Caminho do arquivo
caminho = r"C:\Users\larissa.simas\Documents\lista\ler_texto.txt"

try:
    with open(caminho, "r", encoding="utf-8") as arquivo:
        print("Lendo arquivo linha por linha:\n")

        for numero_linha, linha in enumerate(arquivo, start=1):
            linha = linha.rstrip("\n")   
            print(f"Linha {numero_linha}: {linha}")

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado. Verifique o caminho informado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")