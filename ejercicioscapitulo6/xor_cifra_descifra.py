# fichero xor_cifra_descifra.py
# Cifrado y Descifrado mediante operación XOR
def xor_cifrado(texto, clave):
    resultado = []
    len_clave = len(clave)
    for i, char in enumerate(texto):
        char_clave = clave[i % len_clave]
        # Operación XOR a nivel de bits
        xor_valor = ord(char) ^ ord(char_clave) 
        resultado.append(chr(xor_valor))
    return "".join(resultado)
if __name__ == "__main__":
    try:
        mensaje = input("Introduce el texto: ")
        clave = input("Introduce la clave: ")
        if not clave:
            print("Error: La clave no puede estar vacía.")
        else:
            # Cifrado
            mensaje_cifrado = xor_cifrado(mensaje, clave)
            print("\nTexto Cifrado (Visualización Hexadecimal):")
            hex_output = " ".join(f"{ord(c):02X}" for c in mensaje_cifrado)
            print(hex_output)
            # Descifrado
            mensaje_descifrado = xor_cifrado(mensaje_cifrado, clave)            
            print(f"\nTexto Descifrado (original): {mensaje_descifrado}")    
    except ValueError:
        print("Error en el procesamiento de datos.")