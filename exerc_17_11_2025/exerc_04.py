# 04 Adicionar conteúdo ao final de um arquivo.

# Caminho do arquivo
caminho = r"C:\Users\larissa.simas\Documents\lista\ler_texto.txt"

conteudo_para_adicionar = "\nEsta é uma nova linha adicionada ao final do arquivo."

try:
    
    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(conteudo_para_adicionar)
        print("Conteúdo adicionado ao final do arquivo com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro ao adicionar conteúdo: {e}")