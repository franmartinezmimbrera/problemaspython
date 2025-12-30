# fichero cesar_descifrar.py
# Implementación del Descifrado César (Inversa del desplazamiento)
def descifrar_cesar(mensaje, desplazamiento):
    resultado = ""
    
    for ch in mensaje:
        if ch.isalpha():
            # Determinar la base ('A' o 'a')
            base = ord('A') if ch.isupper() else ord('a')            
            # Fórmula de descifrado: D(x) = (x - n) mod 26
            nuevo_valor = (ord(ch) - base - desplazamiento) % 26            
            resultado += chr(base + nuevo_valor)
        else:
            resultado += ch
            
    return resultado

if __name__ == "__main__":
    
    try:
        mensaje = input("Introduce el mensaje cifrado: ")
        n_input = input("Introduce la clave original (n): ")
        n = int(n_input)
        mensaje_descifrado = descifrar_cesar(mensaje, n)        
        print(f"\nMensaje Descifrado: {mensaje_descifrado}")
        
    except ValueError:
        print("\nError: La clave debe ser un número entero.")