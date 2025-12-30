# fichero cesar_cifrar.py
# Implementación del Cifrado César (Desplazamiento)
def cifrar_cesar(mensaje, desplazamiento):
    resultado = ""
    for ch in mensaje:
        if ch.isalpha():
            # Determinar la base ('A' para mayúsculas, 'a' para minúsculas)
            base = ord('A') if ch.isupper() else ord('a')           
            # Fórmula del cifrado: E(x) = (x + n) mod 26
            # Usamos ord() para convertir char a int y chr() para volver a char
            nuevo_caracter = chr((ord(ch) - base + desplazamiento) % 26 + base)
            resultado += nuevo_caracter
        else:
            resultado += ch
    return resultado
if __name__ == "__main__":
    try:
        mensaje = input("Introduce el mensaje a cifrar: ")
        n_input = input("Introduce el desplazamiento (clave n): ")
        n = int(n_input)
        mensaje_cifrado = cifrar_cesar(mensaje, n)
        print(f"\nMensaje Cifrado: {mensaje_cifrado}")
    except ValueError:
        print("\nError: La clave debe ser un número entero.")