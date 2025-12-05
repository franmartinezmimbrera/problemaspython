# fichero mascara.py
# Invierte (cambia 0->1 y 1->0) los últimos k bits de un número entero

def invertir_bits(numero, k):
    # 1. Crear máscara: (1 desplazado k veces) - 1
    # Ejemplo k=4: 10000 - 1 = 01111
    mascara = (1 << k) - 1
    
    print(f"Original: {bin(numero)} ({numero})")
    print(f"Máscara : {bin(mascara)}")
    
    # 2. Aplicar XOR
    resultado = numero ^ mascara
    
    print(f"Invertido: {bin(resultado)} ({resultado})")
    return resultado

if __name__ == "__main__":
    n = 45 # Ejemplo del enunciado
    k = 4
    invertir_bits(n, k)