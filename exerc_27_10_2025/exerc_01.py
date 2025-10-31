# 1.Tratamento de exceções básicas:
# Escreva um programa que peça ao usuário dois números e faça a divisão do primeiro pelo segundo. 
# Se o usuário inserir um valor inválido ou tentar dividir por zero, o programa deve exibir uma mensagem de erro apropriada.


try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    
    resultado = num1 / num2

except ValueError:
    print("Erro: Por favor, insira apenas números válidos.")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero, tente novamente.")

else:
    print(f"O resultado da divisão é: {resultado:.2f}")

finally:
    print("Programa encerrado.")