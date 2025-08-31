# Faça um programa que:
#  Permita ao usuário adicionar itens a uma lista de compras.Caso o usuário digite "sair", o programa encerra.
# Mostre a lista final de compras organizada em ordem alfabética.

def lista_compras():
    compras = []

    while True:
        item = input("Digite um item para adicionar à lista de compras (ou 'sair' para finalizar): ")
        
        if item.lower() == "sair":
            break
        
        compras.append(item)
    
    
    compras.sort()
    
    print("\nLista de compras finalizada:")
    for i, item in enumerate(compras, 1):
        print(f"{i}. {item}")


lista_compras()

