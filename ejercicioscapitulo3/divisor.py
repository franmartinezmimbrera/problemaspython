# fichero divisor.py
def es_divisor(n, d):
    """Devuelve True si d es divisor de n, False en caso contrario."""
    if d == 0:
        return False # Evitar división por cero
    return n % d == 0

if __name__ == "__main__":
    num = int(input("Introduce el número (N): "))
    div = int(input("Introduce el posible divisor (d): "))
    
    if es_divisor(num, div):
        print(f"{div} ES divisor de {num}.")
    else:
        print(f"{div} NO es divisor de {num}.")