# 01 - Ler todo o conteúdo de um arquivo de texto.

# Caminho do arquivo
caminho = r"C:\Users\larissa.simas\Documents\lista\ler_texto.txt"

try:
    with open(caminho, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado. Verifique o caminho informado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")