import random

def criar_tabuleiro(linhas, colunas, qtd_minas):
    tabuleiro = [[' ' for _ in range(colunas)] for _ in range(linhas)]
    minas = 0
    while minas < qtd_minas:
        l = random.randint(0, linhas - 1)
        c = random.randint(0, colunas - 1)
        if tabuleiro[l][c] != '*':
            tabuleiro[l][c] = '*'
            minas += 1
    return tabuleiro



def contar_minas_vizinhas(tabuleiro, linha, coluna):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    contagem = 0
    for i in range(linha - 1, linha + 2):
        for j in range(coluna - 1, coluna + 2):
            if 0 <= i < linhas and 0 <= j < colunas:
                if tabuleiro[i][j] == '*':
                    contagem += 1
    return contagem



def mostrar_tabuleiro(tabuleiro, revelado):
    print("\n   ", end="")
    for c in range(len(tabuleiro[0])):
        print(f"{c} ", end="")
    print("\n  " + "--" * len(tabuleiro[0]))
    for i in range(len(tabuleiro)):
        print(f"{i}| ", end="")
        for j in range(len(tabuleiro[0])):
            if revelado[i][j]:
                print(tabuleiro[i][j], end=" ")
            else:
                print("#", end=" ")
        print()
    print()



def jogar(linhas=5, colunas=5, qtd_minas=5):
    tabuleiro = criar_tabuleiro(linhas, colunas, qtd_minas)
    revelado = [[False for _ in range(colunas)] for _ in range(linhas)]
    celulas_seguras = linhas * colunas - qtd_minas
    abertas = 0

    while True:
        mostrar_tabuleiro(tabuleiro, revelado)
        try:
            linha = int(input("Digite a linha: "))
            coluna = int(input("Digite a coluna: "))
            if not (0 <= linha < linhas and 0 <= coluna < colunas):
                print("Coordenadas fora do tabuleiro! Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida! Digite números inteiros.")
            continue

        if revelado[linha][coluna]:
            print("Essa posição já foi aberta!")
            continue

        revelado[linha][coluna] = True

        if tabuleiro[linha][coluna] == '*':
            print("\n BOOM! Você encontrou uma mina!")
            for i in range(linhas):
                for j in range(colunas):
                    revelado[i][j] = True
            mostrar_tabuleiro(tabuleiro, revelado)
            print("GAME OVER")
            break

        minas = contar_minas_vizinhas(tabuleiro, linha, coluna)
        tabuleiro[linha][coluna] = str(minas)
        abertas += 1

        if abertas == celulas_seguras:
            mostrar_tabuleiro(tabuleiro, revelado)
            print("Parabéns! Você venceu o jogo!")
            break


print("CAMPO MINADO")
jogar()