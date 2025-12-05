# fichero burbuja.py
def ordenacion_burbuja(lista):
    n = len(lista)
    # Recorremos todos los elementos de la lista
    for i in range(n):
        intercambio = False
        
        # Últimos i elementos ya están ordenados
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        
        # Si no hubo intercambios en la pasada, la lista ya está ordenada
        if not intercambio:
            break
    return lista

if __name__ == "__main__":
    datos = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", datos)
    ordenado = ordenacion_burbuja(datos.copy())
    print("Ordenado (Burbuja):", ordenado)