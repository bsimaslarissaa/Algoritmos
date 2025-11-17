# 06 - Buscar uma palavra em um arquivo e exibir as linhas onde ela aparece.

# Caminho do arquivo
caminho = r"C:\Users\larissa.simas\Documents\lista\ler_texto.txt"


palavra_busca = "conteúdo"

try:
    with open(caminho, "r", encoding="utf-8") as arquivo:
        print(f"Buscando a palavra '{palavra_busca}' no arquivo...\n")

        encontrou = False

        for numero_linha, linha in enumerate(arquivo, start=1):
            if palavra_busca.lower() in linha.lower():  
                print(f"Linha {numero_linha}: {linha.strip()}")
                encontrou = True

        if not encontrou:
            print("A palavra não foi encontrada no arquivo.")

except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o caminho.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")