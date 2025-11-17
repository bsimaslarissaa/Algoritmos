# 07 -  Copiar o conteúdo de um arquivo para outro.

# Ler do (atual) "destino" e escrever em (atual) "origem" — sobrescrevendo
caminho_fonte = r"C:\Users\larissa.simas\Documents\lista\conteudo_para_ser_copiado.txt"
caminho_alvo  = r"C:\Users\larissa.simas\Documents\lista\ler_texto.txt"

try:
    with open(caminho_fonte, "r", encoding="utf-8") as f_fonte:
        conteudo = f_fonte.read()

    with open(caminho_alvo, "w", encoding="utf-8") as f_alvo:
        f_alvo.write(conteudo)

    print("Conteúdo copiado com sucesso (sobrescrito).")

except FileNotFoundError as fnf:
    print(f"Erro: arquivo não encontrado: {fnf.filename}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")