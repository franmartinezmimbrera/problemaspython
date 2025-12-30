# fichero frecuencia.py
# Análisis de Frecuencias de caracteres
# Calcula cuántas veces aparece cada letra y su porcentaje respecto al total.
def analizar_frecuencias(mensaje):
    conteo = [0] * 26
    total_letras = 0    
    for char in mensaje:
        if char.isalpha():
            # Convertimos a minúscula para normalizar
            char_lower = char.lower()            
            # Calculamos el índice (0 para 'a', 1 para 'b', etc.)
            index = ord(char_lower) - ord('a')            
            # Incrementamos el contador en esa posición
            conteo[index] += 1
            total_letras += 1            
    return conteo, total_letras
if __name__ == "__main__":    
    try:
        mensaje = input("Introduce el texto cifrado para analizar: ")
        conteo, total = analizar_frecuencias(mensaje)        
        print("\n Resultados del Análisis \n")
        print(f"Total de letras analizadas: {total}")        
        if total > 0:
            for i in range(26):
                if conteo[i] > 0:
                    porcentaje = (conteo[i] / total) * 100
                    # Recuperamos la letra en mayúscula para mostrarla
                    letra = chr(ord('A') + i)                    
                    print(f"Letra '{letra}': {conteo[i]:3} veces ({porcentaje:.2f}%)")
        else:
            print("No se encontraron letras en el texto.")            
    except Exception as e:
        print(f"Error: {e}")