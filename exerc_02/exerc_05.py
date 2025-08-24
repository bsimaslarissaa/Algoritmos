# Peça ao usuário um número de 11 dígitos e:
# • Verifique se todos os caracteres são dígitos;
# • Verifique se o tamanho é válido (11);
# • Mostre "CPF válido" ou "CPF inválido".
# (Não precisa calcular os dígitos verificadores ainda — é apenas validação estrutural.)

def verificar_cpf():
    cpf = input("Digite o número do CPF (apenas dígitos): ")

    if not cpf.isdigit():
        print("CPF inválido: deve ter apenas números")
        return
    
    if len(cpf) != 11:
        print("CPF inválido: deve ter 11 dígitos")
        return
    
    print("CPF válido")

verificar_cpf()