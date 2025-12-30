# fichero sustitucion.py
# Implementación del Cifrado por Sustitución Monoalfabética
# Utilizamos un alfabeto desordenado (clave) para sustituir al original.
ALFABETO_NORMAL = "abcdefghijklmnopqrstuvwxyz"
ALFABETO_CLAVE  = "qwertyuiopasdfghjklzxcvbnm"

def cifrar_sustitucion(mensaje):
    resultado = []
    for char in mensaje:
        if char.isalpha():
            es_mayuscula = char.isupper()
            char_lower = char.lower()            
            # Buscamos la posición en el alfabeto normal
            if char_lower in ALFABETO_NORMAL:
                posicion = ALFABETO_NORMAL.index(char_lower)                
                # Obtenemos el sustituto del alfabeto clave
                sustituto = ALFABETO_CLAVE[posicion]                
                # Restauramos mayúscula si es necesario
                if es_mayuscula:
                    sustituto = sustituto.upper()
                resultado.append(sustituto)
            else:
                resultado.append(char)
        else:
            resultado.append(char)
    return "".join(resultado)

if __name__ == "__main__":
    print(f"Alfabeto Clave: {ALFABETO_CLAVE}")
    try:
        mensaje = input("Introduce el mensaje a cifrar: ")
        mensaje_cifrado = cifrar_sustitucion(mensaje)
        print(f"Mensaje con Sustitución: {mensaje_cifrado}")
        
    except Exception as e:
        print(f"Error: {e}")