def voltear_matriz_horizontal(matriz):
    
    filas = len(matriz)
    columnas = len(matriz[0])

    
    matriz_volteada = []

    
    for fila in matriz:
        fila_volteada = fila[::-1]  
        matriz_volteada.append(fila_volteada)

    return matriz_volteada


matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_volteada = voltear_matriz_horizontal(matriz_original)


print("Matriz original:")
for fila in matriz_original:
    print(fila)

print("\nMatriz volteada horizontalmente:")
for fila in matriz_volteada:
    print(fila)