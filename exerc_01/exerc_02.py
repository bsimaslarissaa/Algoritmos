# Questão 02: Escreva um algoritmo que calcule a tabuada de um número digitado pelo usuário.

n = int(input("Digite um número para ver a tabuada: "))

print(f"A tabuada de {n}")
for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")