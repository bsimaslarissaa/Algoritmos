# 4.Exceções personalizadas: Escreva uma função que verifica se uma senha possui no mínimo 8 caracteres e pelo menos um número. 
# Se a senha não atender aos requisitos, levante uma exceção com uma mensagem personalizada.
# Trate a exceção e mostre a mensagem ao usuário.

class SenhaInvalida(Exception):
    pass

def verificar_senha(senha):
    if len(senha) < 8 or not any(c.isdigit() for c in senha):
        raise SenhaInvalida("A senha deve ter pelo menos 8 caracteres e conter um número.")
    print("Senha válida!")

try:
    senha = input("Digite sua senha: ")
    verificar_senha(senha)
except SenhaInvalida as e:
    print(f"Erro: {e}")