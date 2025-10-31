# 5.Simulação de transações: Crie um programa que simule uma transferência bancária.
# Peça ao usuário o saldo da conta e o valor da transferência. 
# Caso o saldo seja insuficiente, levante uma exceção do tipo ValueError com a mensagem "Saldo insuficiente".
# Trate a exceção adequadamente e informe o usuário.

def transferencia(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente.")
    print("Transferência realizada com sucesso!")

try:
    saldo = float(input("Digite o saldo da conta: "))
    valor = float(input("Digite o valor da transferência: "))
    transferencia(saldo, valor)
except ValueError as e:
    print(f"Erro: {e}")