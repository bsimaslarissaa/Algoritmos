"""
    Implementação do algoritmo Selection Sort (Ordenação por Seleção).
    Percorre o array, encontra o menor elemento na parte não ordenada
    e o coloca na posição correta.
    
    Vantagens:
    - Simples de implementar e entender
    - Não requer memória extra (ordenação in-place)
    - Bom para listas pequenas ou quando a escrita em memória é cara
    - Número fixo de trocas (O(n)), útil se trocas forem custosas
    
    Desvantagens:
    - Complexidade O(n²) mesmo no melhor caso
    - Não é estável (elementos iguais podem trocar de ordem)
    - Ineficiente para grandes conjuntos de dados
    - Não é adaptativo (não aproveita ordenação parcial existente)
"""

def selection_sort(arr): 
    n = len(arr) 

    for i in range(n - 1):  

        indice_menor = i  
        for j in range(i + 1, n):  
            if arr[j] < arr[indice_menor]:  
                indice_menor = j

        if indice_menor != i: 
            arr[i], arr[indice_menor] = arr[indice_menor], arr[i]  

    return arr

lista = [64, 34, 25, 12, 22, 11, 90]
print("antes:", lista)
selection_sort(lista)
print("depois", lista)