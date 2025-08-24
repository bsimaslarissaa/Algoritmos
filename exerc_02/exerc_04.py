# Dada uma lista de nomes, implemente uma função que busque um nome digitado pelo usuário.
# Informe a posição em que ele aparece ou diga que não foi encontrado.

nomes = ["Larissa", "Vanessa", "Marcos", "Gioliano", "Carlos"]

def buscar_nome_simples(lista_nomes):
    nome_busca = input("Digite o nome que deseja buscar: ").strip()

    try:
        posicao = lista_nomes.index(nome_busca)
        print(f"O nome '{nome_busca}' foi encontrado na posição {posicao}")
    except ValueError:
        print(f"O nome '{nome_busca}' não foi encontrado na lista.")
        
buscar_nome_simples(nomes)