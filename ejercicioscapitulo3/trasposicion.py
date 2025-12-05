# fichero trasposicion.py
# Función para trasponer una matriz MxN
def imprimir_matriz(m):
    for fila in m:
        print(fila)

def trasponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Crear matriz vacía para el resultado (Columnas x Filas)
    matriz_T = [[0] * filas for _ in range(columnas)]
    
    for i in range(filas):
        for j in range(columnas):
            matriz_T[j][i] = matriz[i][j]
            
    return matriz_T

if __name__ == "__main__":
    # Matriz 2x3 de ejemplo
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    print("Matriz Original:")
    imprimir_matriz(A)
    
    AT = trasponer_matriz(A)
    
    print("\nMatriz Traspuesta:")
    imprimir_matriz(AT)