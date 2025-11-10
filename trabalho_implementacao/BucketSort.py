
# Bucket Sort
# Vantagens:
# - Muito eficiente quando os dados estão uniformemente distribuídos.
# - Complexidade média O(n + k).
# Desvantagens:
# - Funciona melhor com dados decimais entre 0 e 1.
# - Depende da escolha do tamanho e número de baldes.

def bucket_sort(arr):
    bucket = [[] for _ in range(len(arr))]

    for num in arr:
        index = int(num * len(arr))
        bucket[index].append(num)

    for b in bucket:
        b.sort()

    result = []
    for b in bucket:
        result.extend(b)
    return result

lista = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print(bucket_sort(lista))
