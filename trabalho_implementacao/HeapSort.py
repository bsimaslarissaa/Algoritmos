
def heapify(arr, n, i):
    maior = i
    e, d = 2*i + 1, 2*i + 2

    if e < n and arr[e] > arr[maior]:
        maior = e
    if d < n and arr[d] > arr[maior]:
        maior = d

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)


def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# Exemplo de uso
valores = [12, 11, 13, 5, 6, 7]
heap_sort(valores)
print(valores)