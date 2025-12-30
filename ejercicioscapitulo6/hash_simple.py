# fichero hash_simple.py
# Implementación de una función Hash simple (Estilo K&R)
# Transforma una cadena en un valor numérico único.
def generar_hash_kr(texto):
    hashval = 0
    for char in texto:
        # Algoritmo K&R: hash = hash * 31 + c
        hashval = ord(char) + 31 * hashval   
        # Python maneja enteros infinitos. Para que esto se comporte como un hash 
        # de tamaño fijo y haga "overflow", aplicamos una máscara de 64 bits.
        hashval = hashval & 0xFFFFFFFFFFFFFFFF
        
    return hashval

if __name__ == "__main__":  
    try:
        entrada = input("Introduce un texto para generar su Hash: ")
        if not entrada:
            print("Advertencia: Has introducido una cadena vacía.")
            
        hash_value = generar_hash_kr(entrada)
        print(f"Entrada: {entrada}")
        print(f"Hash calculado (Hex): {hash_value:X}")
        print(f"Hash calculado (Dec): {hash_value}")
        
    except Exception as e:
        print(f"Error: {e}")