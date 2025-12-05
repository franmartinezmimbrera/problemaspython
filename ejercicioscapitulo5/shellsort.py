# fichero shellsort.py

def shellsort_knuth(lista):
    n = len(lista)
    
    # 1. Calcular el intervalo inicial según Knuth (h = 3*h + 1)
    h = 1
    while h < n // 3:
        h = 3 * h + 1
    
    # 2. Iterar reduciendo el intervalo
    while h >= 1:
        # Ordenación por inserción con saltos de tamaño h
        for i in range(h, n):
            temp = lista[i]
            j = i
            
            while j >= h and lista[j - h] > temp:
                lista[j] = lista[j - h]
                j -= h
            
            lista[j] = temp
        
        # Reducir intervalo (inverso de Knuth)
        h //= 3
        
    return lista

if __name__ == "__main__":
    datos = [12, 34, 54, 2, 3]
    print("Original:", datos)
    print("Ordenado (ShellSort Knuth):", shellsort_knuth(datos.copy()))