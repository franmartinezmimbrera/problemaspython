## fichero heapsort.py

def heapify(lista, n, i):
    mas_grande = i      # Inicializar el más grande como raíz
    izq = 2 * i + 1     # Hijo izquierdo
    der = 2 * i + 2     # Hijo derecho
    
    # Ver si hijo izquierdo existe y es mayor que la raíz
    if izq < n and lista[izq] > lista[mas_grande]:
        mas_grande = izq
        
    # Ver si hijo derecho existe y es mayor que el más grande hasta ahora
    if der < n and lista[der] > lista[mas_grande]:
        mas_grande = der
        
    # Si la raíz no es el más grande, intercambiar
    if mas_grande != i:
        lista[i], lista[mas_grande] = lista[mas_grande], lista[i]
        
        # Recursivamente hacer heapify en el subárbol afectado
        heapify(lista, n, mas_grande)

def heapsort(lista):
    n = len(lista)
    
    # 1. Construir el Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
        
    # 2. Extraer elementos uno a uno
    for i in range(n - 1, 0, -1):
        # Mover la raíz actual (máximo) al final
        lista[i], lista[0] = lista[0], lista[i]
        # Llamar heapify en el heap reducido
        heapify(lista, i, 0)
        
    return lista

if __name__ == "__main__":
    datos = [12, 11, 13, 5, 6, 7]
    print("Original:", datos)
    print("Ordenado (HeapSort):", heapsort(datos.copy()))
