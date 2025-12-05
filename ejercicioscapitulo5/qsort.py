# fichero qsort.cpp 

def quicksort(lista):
    # Caso base: listas de 0 o 1 elemento ya están ordenadas
    if len(lista) <= 1:
        return lista
    
    # Elegimos el pivote (aquí tomamos el último elemento)
    pivote = lista[-1]
    
    # Partición
    menores = [x for x in lista[:-1] if x <= pivote]
    mayores = [x for x in lista[:-1] if x > pivote]
    
    # Llamada recursiva
    return quicksort(menores) + [pivote] + quicksort(mayores)

if __name__ == "__main__":
    datos = [10, 7, 8, 9, 1, 5]
    print("Original:", datos)
    print("Ordenado (Quicksort):", quicksort(datos))