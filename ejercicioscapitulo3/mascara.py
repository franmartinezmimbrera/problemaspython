# fichero mascara.py
# Invierte (cambia 0->1 y 1->0) los últimos k bits de un número entero
def invertir_bits(numero, k):
    mascara = (1 << k) - 1
    
    print(f"Original: {bin(numero)} ({numero})")
    print(f"Máscara : {bin(mascara)}")
    resultado = numero ^ mascara
    print(f"Invertido: {bin(resultado)} ({resultado})")
    return resultado

if __name__ == "__main__":
    n = 45 # Ejemplo del enunciado
    k = 4
    invertir_bits(n, k)