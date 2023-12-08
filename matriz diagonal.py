import numpy as np

def crear_matriz_diagonal(tamano):
    matriz = np.diag(np.arange(1, tamano + 1))
    return matriz

def sumar_elementos(matriz):
    suma = np.sum(np.diag(matriz))
    return suma


def multiplicar_elementos(matriz):
    producto = np.prod(np.diag(matriz))
    return producto


tamano_matriz = 5
matriz_diagonal = crear_matriz_diagonal(tamano_matriz)

print("Matriz diagonal:")
print(matriz_diagonal)

suma_elementos = sumar_elementos(matriz_diagonal)
producto_elementos = multiplicar_elementos(matriz_diagonal)

print("\nSuma de elementos en la diagonal:", suma_elementos)
print("Producto de elementos en la diagonal:", producto_elementos)