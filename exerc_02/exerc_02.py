# Questão 2:Implemente um algoritmo que simule um sistema de login:
# • O usuário tem 3 tentativas para digitar a senha correta (senha123).
# • Caso erre todas, mostre "Acesso bloqueado".
# • Caso acerte, mostre "Bem-vindo!".

senha_correta = "admin123"
tentativas = 3

while tentativas > 0:
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Bem-vindo!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha incorreta. Você ainda tem {tentativas} tentativa(s).")
        else:
            print("Acesso bloqueado")




