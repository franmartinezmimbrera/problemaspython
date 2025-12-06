#fichero radixsort.py
def counting_sort_para_radix(lista, exp):
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10 # Base 10 (dígitos 0-9)
    # Contar ocurrencias según el dígito actual (exp)
    for i in range(n):
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1
    # Calcular posiciones reales en salida
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]
    # Construir el array de salida (recorriendo hacia atrás para estabilidad)
    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1 
    # Copiar al original
    for i in range(n):
        lista[i] = salida[i]

def radixsort(lista):
    if not lista:
        return lista
    # Encontrar el número máximo para saber cantidad de dígitos
    maximo = max(lista)
    # Aplicar counting sort para cada posición decimal (1, 10, 100...)
    exp = 1
    while maximo // exp > 0:
        counting_sort_para_radix(lista, exp)
        exp *= 10
    return lista

if __name__ == "__main__":
    datos = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original:", datos)
    print("Ordenado (RadixSort):", radixsort(datos.copy()))