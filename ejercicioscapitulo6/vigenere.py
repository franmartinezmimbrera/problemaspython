# fichero vigenere.py
# Implementación del Cifrado de Vigenere (Polialfabético)
def cifrar_vigenere(mensaje, clave):
    resultado = []
    len_clave = len(clave)    
    # Si la clave está vacía, devolvemos el mensaje tal cual
    if len_clave == 0:
        return mensaje    
    # Aseguramos que la clave esté en mayúsculas para simplificar el cálculo del desplazamiento
    clave = clave.upper()    
    indice_clave = 0  
    for char in mensaje:
        if char.isalpha():
            # Determinar la base ('A' o 'a')
            base = ord('A') if char.isupper() else ord('a')            
            # Calculamos el desplazamiento 'k' basado en la letra actual de la clave
            # Restamos 'A' para obtener un valor entre 0 y 25
            char_clave = clave[indice_clave % len_clave]
            k = ord(char_clave) - ord('A')            
            # Fórmula Vigenere: C = (M + K) mod 26
            nuevo_valor = (ord(char) - base + k) % 26            
            resultado.append(chr(base + nuevo_valor))            
            # Avanzamos el índice de la clave SOLO si hemos cifrado una letra
            indice_clave += 1
        else:
            # Si no es letra, se añade sin cambios y NO avanzamos el índice de la clave
            resultado.append(char)            
    return "".join(resultado)
if __name__ == "__main__":
    try:
        mensaje = input("Introduce el mensaje: ")
        clave_input = input("Introduce la palabra clave (solo letras): ")        
        # Limpiamos la clave para quedarnos solo con letras (para evitar errores matemáticos)
        clave = "".join(c for c in clave_input if c.isalpha())        
        if not clave:
            print("Error: La clave debe contener al menos una letra.")
        else:
            mensaje_cifrado = cifrar_vigenere(mensaje, clave)
            print(f"\nMensaje Cifrado Vigenere: {mensaje_cifrado}")            
    except Exception as e:
        print(f"Error inesperado: {e}")