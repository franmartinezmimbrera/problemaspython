# fichero qsort2.py

def ordenacion_timsort_nativa(lista):
    # Python utiliza TimSort en sus métodos built-in
    # Opción A: sorted() devuelve una nueva lista ordenada
    nueva_lista = sorted(lista)
    return nueva_lista

if __name__ == "__main__":
    datos = [34, 2, 15, 88, 1, 60]
    print("Original:", datos)
    
    resultado = ordenacion_timsort_nativa(datos)
    
    print("Ordenado (Python/TimSort):", resultado)
