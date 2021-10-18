matriz = [[0,0,0],[0,0,0],[0,0,0]]
acerto1 = 0
colunas = []
ganhou = False
while ganhou != True:
    print('Jogador 1')
    for valor in matriz:
        print(valor)
        linha = int(input('Escolha uma linha de 1 a 3\n'))
        coluna = int(input('Escolha uma coluna de 1 a 3\n'))
        matriz[linha-1][coluna-1] = 'x'
    for valor in matriz:
        print(f'{valor}')
        if valor.count('x') == 3:
            print('Ganhou')
            ganhou = True
    for i in range(0,3):
        colunas.append(matriz[0][i])
        colunas.append(matriz[1][i])
        colunas.append(matriz[2][i])
        if colunas.count('x') == 3:
            print('ganhou')
            ganhou = True
        else:
            colunas.clear()
            diagonal1 = []
            diagonal1.append(matriz[0][0])
            diagonal1.append(matriz[1][1])
            diagonal1.append(matriz[2][2])
            diagonal2 = []
            diagonal2.append(matriz[0][2])
            diagonal2.append(matriz[1][1])
            diagonal2.append(matriz[2][0])
        if diagonal1.count('x') == 3 or diagonal2.count('x') == 3:
            print('ganhou')
            ganhou = True
            diagonal1.clear()
            diagonal2.clear()
    if ganhou == True:
            break
            print('-'*30)
            print('Jogador 2')
    for valor in matriz:
        print(valor)
        linha = int(input('Escolha uma linha de 1 a 3n\n'))
        coluna = int(input('Escolha uma coluna de 1 a 3\n'))
        matriz[linha-1][coluna-1] = 'o'
    for valor in matriz:
        print(f'{valor}')
        if valor.count('o') == 3:
            print('Ganhou')
            ganhou = True
    for i in range(0,3):
        colunas.append(matriz[0][i])
        colunas.append(matriz[1][i])
        colunas.append(matriz[2][i])
        if colunas.count('o') == 3:
            print('ganhou')
            ganhou = True
        else:
            colunas.clear()
            diagonal1 = []
            diagonal1.append(matriz[0][0])
            diagonal1.append(matriz[1][1])
            diagonal1.append(matriz[2][2])
            diagonal2 = []
            diagonal2.append(matriz[0][2])
            diagonal2.append(matriz[1][1])
            diagonal2.append(matriz[2][0])
        if diagonal1.count('x') == 3 or diagonal2.count('x') == 3:
            print('ganhou')
            ganhou = True
            diagonal1.clear()
            diagonal2.clear()

