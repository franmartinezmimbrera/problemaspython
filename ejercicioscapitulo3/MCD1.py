#fichero MCD1.py 
def mcd_euclides(a, b):
    while b > 0:
        a, b = b, a % b
    return a
if __name__ == "__main__":
    try:
        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))
        resultado = mcd_euclides(n1, n2)
        print(f"El MCD calculado por función es: {resultado}")
    except ValueError:
        print("Error en la entrada de datos.")