# fichero multiplicamatrices.py

def multiplicar_matrices(A, B):
    # Asumimos matrices cuadradas NxN para este ejercicio
    N = len(A)
    
    # Crear matriz resultado vacía
    C = [[0] * N for _ in range(N)]
    
    for i in range(N):           # Recorre filas de A
        for j in range(N):       # Recorre columnas de B
            suma = 0
            for k in range(N):   # Producto escalar
                suma += A[i][k] * B[k][j]
            C[i][j] = suma
            
    return C

if __name__ == "__main__":
    # Matrices 2x2
    m1 = [[1, 2], [3, 4]]
    m2 = [[2, 0], [1, 2]]
    
    print("Matriz A:", m1)
    print("Matriz B:", m2)
    
    res = multiplicar_matrices(m1, m2)
    
    print("Resultado A*B:")
    for fila in res:
        print(fila)