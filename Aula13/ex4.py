# Lista dentro de lista (ou matriz)

# Uma matriz 3x3 (3 linhas e 3 colunas)
matriz = [
    [1, 2, 3],  # Linha 0
    [4, 5, 6],  # Linha 1
    [7, 8, 9],  # Linha 2
]

# Acessar a matriz: matriz[linha][coluna]
print(matriz[0][0])  
print(matriz[1][2])  


# Percorrendo todos os elementos
print ("Percorrendo uma matriz")
for linha in matriz:
    for coluna in linha:
        print(coluna, end = " ")  
    print () #Pular linha