# fichero multiplicamatrices.py
def multiplicar_matrices(A, B):
    N = len(A)
    C = [[0] * N for _ in range(N)]
    for i in range(N):          
        for j in range(N):       
            suma = 0
            for k in range(N):   
                suma += A[i][k] * B[k][j]
            C[i][j] = suma      
    return C
if __name__ == "__main__":
    m1 = [[1, 2], [3, 4]]
    m2 = [[2, 0], [1, 2]]
    
    print("Matriz A:", m1)
    print("Matriz B:", m2)
    res = multiplicar_matrices(m1, m2)
    print("Resultado A*B:")
    for fila in res:
        print(fila)