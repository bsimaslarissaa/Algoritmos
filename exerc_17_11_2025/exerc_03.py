# 03 - Escrever conteúdo em um arquivo (sobrescrevendo).

# Caminho do arquivo
caminho = r"C:\Users\larissa.simas\Documents\lista\ler_texto.txt"

novo_conteudo = """
Olá! Este é um novo conteúdo escrito no arquivo.
Todo conteúdo anterior foi sobrescrito.
"""

try:
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(novo_conteudo.strip())
        print("Arquivo sobrescrito com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro ao escrever no arquivo: {e}")