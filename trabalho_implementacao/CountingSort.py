
# Counting Sort
# Vantagens:
# - Muito rápido para listas com números inteiros pequenos.
# - Complexidade O(n + k), onde k é o maior valor.
# - Estável.
# Desvantagens:
# - Não funciona com números negativos ou dados não inteiros sem adaptação.
# - Usa muita memória se o maior valor for muito grande.

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1
    return arr

lista = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(lista))
