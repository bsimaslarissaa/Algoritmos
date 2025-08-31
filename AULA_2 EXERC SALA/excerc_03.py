# 1. Receba 10 números inteiros digitados pelo usuário.
#  Separe-os em duas listas: pares e ímpares. Exiba quantos números pares e ímpares foram digitados.

def separar_pares_impares():
    pares = []  
    impares = []  

    
    for i in range(10):
        numero = int(input(f"Digite o {i + 1}º número inteiro: "))
        

        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    
    print(f"\nNúmeros pares digitados: {pares}")
    print(f"Números ímpares digitados: {impares}")
    print(f"Quantidade de números pares: {len(pares)}")
    print(f"Quantidade de números ímpares: {len(impares)}")

separar_pares_impares()
