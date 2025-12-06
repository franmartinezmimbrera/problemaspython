# fichero shellsort.py
def shellsort_knuth(lista):
    n = len(lista)  
    h = 1
    while h < n // 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, n):
            temp = lista[i]
            j = i
            while j >= h and lista[j - h] > temp:
                lista[j] = lista[j - h]
                j -= h
            
            lista[j] = temp        
        h //= 3        
    return lista
if __name__ == "__main__":
    datos = [12, 34, 54, 2, 3]
    print("Original:", datos)
    print("Ordenado (ShellSort Knuth):", shellsort_knuth(datos.copy()))