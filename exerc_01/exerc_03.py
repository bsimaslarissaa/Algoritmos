# Questão 03: Crie uma função que verifique se um número é primo.

num = int(input('Digite um número:'))
div = 0
for cont in range(1, num + 1):
    if num % cont == 0:
        div += 1
if div == 2: 
    print ('Seu número é primo')
else:
    print ('Seu número não é primo')
    
     


