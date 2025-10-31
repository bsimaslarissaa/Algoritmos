# 3.Bloco else e finally: Escreva um programa que solicite um número ao usuário. 
# Se o número for maior que 10, exiba uma mensagem dizendo que o número é válido.
#  Utilize o bloco else para imprimir que o programa foi executado com sucesso, e o bloco finally para imprimir "Programa encerrado#.


try:
   
    numero = float(input("Digite um número: "))

    if numero > 10:
        print("O número é válido pois é maior que 10.")
    else:
        print("O número não é maior que 10.")

except ValueError:
    print("Erro: Por favor, insira um número válido.")

else:
    print("Programa executado com sucesso!")

finally:
    print("Programa encerrado.")