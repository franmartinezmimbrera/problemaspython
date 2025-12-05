#fichero mergesort.py

def mergesort(lista):
    if len(lista) <= 1:
        return lista

    # División
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])

    # Fusión (Merge)
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    
    # Comparar elementos y ordenarlos
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
            
    # Añadir los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

if __name__ == "__main__":
    datos = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", datos)
    print("Ordenado (Mergesort):", mergesort(datos))