# fichero cesar_bruta.py
# Ataque de fuerza bruta al Cifrado César
# Prueba todas las claves posibles (1-25) para que el usuario identifique el mensaje
def imprimir_intento(mensaje, key):
    resultado = ""
    for ch in mensaje:
        if ch.isalpha():
            # Determinar si es mayúscula o minúscula
            base = ord('A') if ch.isupper() else ord('a')            
            # Fórmula de descifrado: D(x) = (x - key) mod 26
            nuevo_valor = (ord(ch) - base - key) % 26            
            resultado += chr(base + nuevo_valor)
        else:
            resultado += ch
            
    print(f"Clave {key:2}: {resultado}")

if __name__ == "__main__":
    
    try:
        mensaje = input("Introduce el texto cifrado para atacar por fuerza bruta: ")
        print("\n Resultados del Criptoanálisis \n")
        # Bucle para probar todas las rotaciones posibles (del 1 al 25)
        for k in range(1, 26):
            imprimir_intento(mensaje, k)
            
    except KeyboardInterrupt:
        print("\nOperación cancelada.")