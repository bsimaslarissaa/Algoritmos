# Questao 1: Escreva um algoritmo que conte quantas operações básicas (somas) são executadas para calcular a soma dos números de 1 até n. Exiba o resultado e compare com a fórmula matemática n*(n+1)/2.

n = int(input('Digite um número:'))
soma = 0
qtd_somas = 0
for cont in range(1, n + 1):
    soma = soma + cont
    qtd_somas += 1
print (f'O valor das somas é de {soma}')
print (f'A quantidade de operações de adição é de {qtd_somas}')

# Comparação com a fómula

formula = n * (n + 1) // 2
somas = 0
print(f"O valor das somas pela fórmula é de {formula}")
print(f"A quantidade de operações de adição pelo método da função é de {somas}")