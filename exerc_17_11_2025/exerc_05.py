# 05 Contar o número de linhas em um arquivo.

# Caminho do arquivo
caminho = r"C:\Users\larissa.simas\Documents\lista\ler_texto.txt"

try:
    with open(caminho, "r", encoding="utf-8") as arquivo:
        quantidade_linhas = sum(1 for _ in arquivo)

    print(f"O arquivo possui {quantidade_linhas} linhas.")

except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o caminho.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")