# fichero binterpola.py
def busqueda_interpolacion(lista, objetivo):
    #Requiere lista ORDENADA y distribución UNIFORME.
   
    bajo = 0
    alto = len(lista) - 1
    
    while bajo <= alto and objetivo >= lista[bajo] and objetivo <= lista[alto]:
        if bajo == alto:
            if lista[bajo] == objetivo:
                return bajo
            return -1
        
        # Fórmula de interpolación para estimar posición
        # pos = lo + [ (x-arr[lo]) * (hi-lo) / (arr[hi]-arr[lo]) ]
        pos = bajo + int(((float(alto - bajo) / (lista[alto] - lista[bajo])) * (objetivo - lista[bajo])))
        
        if lista[pos] == objetivo:
            return pos
            
        if lista[pos] < objetivo:
            bajo = pos + 1
        else:
            alto = pos - 1
            
    return -1

if __name__ == "__main__":
    # Funciona mejor con datos uniformemente distribuidos
    datos = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    buscado = 70
    
    idx = busqueda_interpolacion(datos, buscado)
    
    if idx != -1:
        print(f"Elemento {buscado} encontrado en índice {idx} mediante interpolación.")
    else:
        print("Elemento no encontrado.")