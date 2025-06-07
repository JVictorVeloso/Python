from random import randrange

def exibir_tabuleiro(tabuleiro):
    print('+-------+-------+-------+')
    for linha in tabuleiro:
        print('|       |       |       |')
        print(f'|   {linha[0]}   |   {linha[1]}   |   {linha[2]}   |')
        print('|       |       |       |')
        print('+-------+-------+-------+')

def movimentos_livres(tabuleiro):
    livres = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] not in ['X', 'O']:
                livres.append((i, j))
    return livres

def vitoria(tabuleiro, jogador):
    # Checa linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
        if all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    # Checa diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    return False

def empate(tabuleiro):
    return all(tabuleiro[i][j] in ['X', 'O'] for i in range(3) for j in range(3))

def movimento_usuario(tabuleiro):
    while True:
        try:
            movimento = int(input('Digite seu movimento: '))
            if movimento < 1 or movimento > 9:
                print('Movimento inválido. Tente novamente.')
                continue
            linha = (movimento - 1) // 3
            coluna = (movimento - 1) % 3
            if tabuleiro[linha][coluna] in ['X', 'O']:
                print('Campo já ocupado. Tente novamente.')
                continue
            tabuleiro[linha][coluna] = 'O'
            break
        except ValueError:
            print('Por favor, digite um número inteiro válido.')

def movimento_computador(tabuleiro):
    livres = movimentos_livres(tabuleiro)
    if livres:
        i, j = livres[randrange(len(livres))]
        tabuleiro[i][j] = 'X'

def main():
    # Inicializa o tabuleiro
    tabuleiro = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    # Primeiro movimento do computador
    tabuleiro[1][1] = 'X'
    while True:
        exibir_tabuleiro(tabuleiro)
        if vitoria(tabuleiro, 'X'):
            print('O computador ganhou!')
            break
        if empate(tabuleiro):
            print('Empate!')
            break
        movimento_usuario(tabuleiro)
        exibir_tabuleiro(tabuleiro)
        if vitoria(tabuleiro, 'O'):
            print('Você ganhou!')
            break
        if empate(tabuleiro):
            print('Empate!')
            break
        movimento_computador(tabuleiro)

if __name__ == '__main__':
    main()



