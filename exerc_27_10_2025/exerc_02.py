# 2.Capturando exceções múltiplas: Crie um programa que peça ao usuário o nome de uma cor
# e mostre seu valor em RGB de acordo com um dicionário pré-definido. 
# O programa deve tratar exceções caso o nome da cor não exista no dicionário.


cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}

try:
   
    cor = input("Digite o nome de uma cor (vermelho, verde, azul): ").strip().lower()
    
    rgb = cores[cor]
    
except KeyError:
    
    print("Erro: Essa cor não está disponível no dicionário.")
    
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    
else:
    print(f"A cor '{cor}' tem o valor RGB: {rgb}")
    
finally:
    print("Programa encerrado.")