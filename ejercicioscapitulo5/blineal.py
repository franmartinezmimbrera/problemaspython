# fichero blineal.py 

def busqueda_lineal(lista, objetivo):
    #Devuelve el  índice del elemento o -1 si no existe.
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

if __name__ == "__main__":
    datos = [10, 50, 30, 70, 80, 20, 90, 40]
    buscado = 30
    
    posicion = busqueda_lineal(datos, buscado)
    
    if posicion != -1:
        print(f"Número {buscado} encontrado en índice {posicion}.")
    else:
        print(f"Número {buscado} no encontrado.")