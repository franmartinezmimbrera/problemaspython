# fichero transposicion.py
# Implementación del Cifrado por Transposición Columnar
def cifrar_transposicion(mensaje, columnas):
    longitud = len(mensaje)
    filas = (longitud + columnas - 1) // columnas
    resultado = []    
    # Recorremos columna por columna
    for c in range(columnas):
        # Y dentro de cada columna, bajamos por las filas
        for f in range(filas):
            # Calculamos el índice como si fuera una matriz aplanada
            index = f * columnas + c            
            # Verificamos que no nos salimos del mensaje
            if index < longitud:
                resultado.append(mensaje[index])                
    return "".join(resultado)
if __name__ == "__main__":    
    try:
        entrada = input("Introduce el mensaje (sin espacios): ")
        mensaje = entrada.replace(" ", "")        
        columnas_input = input("Introduce el número de columnas (clave): ")
        columnas = int(columnas_input)        
        if columnas < 1:
            print("Error: Las columnas deben ser al menos 1.")
        else:
            cifrado = cifrar_transposicion(mensaje, columnas)            
            print(f"\nMensaje Original:    {mensaje}")
            print(f"Mensaje Transpuesto: {cifrado}")
            
    except ValueError:
        print("\nError: La clave debe ser un número entero.")