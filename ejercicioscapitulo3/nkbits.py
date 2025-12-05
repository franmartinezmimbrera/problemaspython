# fichero nkbits.py 
# Procedimiento que escribe por pantalla los últimos k bits de un número entero.
def mostrar_k_bits(numero, k):
    print(f"Número: {numero} (Binario: {bin(numero)})")
    print(f"Los últimos {k} bits son:")
    
    # Recorremos desde el bit K-1 hasta el 0 (de izquierda a derecha en los inferiores)
    # O simplemente de 0 a K-1 e imprimimos
    bits_str = ""
    for i in range(k):
        # Desplazar el bit 'i' a la posición 0 y hacer AND con 1 para extraerlo
        bit = (numero >> i) & 1
        bits_str = str(bit) + bits_str # Prependemos para que se lea en orden correcto
        
    print(f"Bits: {bits_str}")

if __name__ == "__main__":
    num = int(input("Introduce un número entero: "))
    bits = int(input("Cuántos bits inferiores mostrar: "))
    mostrar_k_bits(num, bits)