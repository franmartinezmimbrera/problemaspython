# fichero bbinaria.py
def busqueda_binaria(lista, objetivo):

    #Requiere que la lista esté ORDENADA. Devuelve el índice o -1.

    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        # Caso 1: Encontrado
        if lista[medio] == objetivo:
            return medio
            
        # Caso 2: El objetivo es mayor, ignorar mitad izquierda
        elif lista[medio] < objetivo:
            izquierda = medio + 1
            
        # Caso 3: El objetivo es menor, ignorar mitad derecha
        else:
            derecha = medio - 1
            
    return -1

if __name__ == "__main__":
    # La lista debe estar ordenada para búsqueda binaria
    datos_ordenados = [2, 3, 4, 10, 40, 55, 60, 70]
    buscado = 10
    
    pos = busqueda_binaria(datos_ordenados, buscado)
    
    if pos != -1:
        print(f"Número {buscado} encontrado en índice {pos}.")
    else:
        print("Número no encontrado.")