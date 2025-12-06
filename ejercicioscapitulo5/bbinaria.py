# fichero bbinaria.py
def busqueda_binaria(lista, objetivo):

    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1 
    return -1

if __name__ == "__main__":
    datos_ordenados = [2, 3, 4, 10, 40, 55, 60, 70]
    buscado = 10
    
    pos = busqueda_binaria(datos_ordenados, buscado)
    
    if pos != -1:
        print(f"Número {buscado} encontrado en índice {pos}.")
    else:
        print("Número no encontrado.")