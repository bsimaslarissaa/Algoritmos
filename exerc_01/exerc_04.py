# Questão 4: Desenvolva um programa que leia uma lista de números e mostre a média deles.

qtd = int(input("Quantos números deseja digitar? "))

numeros = []

for i in range(qtd):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)


media = sum(numeros) / qtd

print("Números digitados:", numeros)
print(f"Média = {media:.2f}")