# fichero leelongi.py
# Este ejercicio lee una cadena desde teclado y dice la longitud y la concatena con otra.

def operaciones_string():
    
    cadena = input("Introduce una cadena: ")
    
    # Longitud
    longitud = len(cadena)
    print(f"La longitud es: {longitud}")
    
    # Concatenación
    nueva_cadena = cadena + ".txt"
    print(f"Concatenada: {nueva_cadena}")

if __name__ == "__main__":
    operaciones_string()