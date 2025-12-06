# fichero invierte.py
#Este ejercicio implementa la inversión de una cadena de texto dada

def invertir_manual(cadena):
    # En Python las cadenas son inmutables, así que las convertimos a lista
    lista_caracteres = list(cadena)
    inicio = 0
    fin = len(lista_caracteres) - 1
    
    # Bucle Swap
    while inicio < fin:
        temp = lista_caracteres[inicio]
        lista_caracteres[inicio] = lista_caracteres[fin]
        lista_caracteres[fin] = temp
        
        inicio += 1
        fin -= 1
        
    # Convertir lista de vuelta a cadena
    return "".join(lista_caracteres)

if __name__ == "__main__":
    texto = input("Introduce texto: ")
    invertido = invertir_manual(texto)
    print(f"Texto invertido: {invertido}")