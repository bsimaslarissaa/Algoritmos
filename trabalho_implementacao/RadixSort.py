
# Radix Sort
# Vantagens:
# - Muito eficiente para números inteiros grandes.
# - Complexidade O(nk), onde k é o número de dígitos.
# - Estável.
# Desvantagens:
# - Funciona apenas para inteiros ou dados que podem ser transformados em inteiros.
# - Usa memória extra.

def counting_sort_exp(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n -1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] -1] = arr[i]
        count[index] -=1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_exp(arr, exp)
        exp *= 10
    return arr

lista = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(lista))
