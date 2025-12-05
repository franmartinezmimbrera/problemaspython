# fichero sumanumerosnaturales.py
#  Este programa calcula la suma de los "n" primeros números naturales con for
def suma_bucle():
    n = int(input("Introduce N (cantidad de números a sumar): "))
    suma = 0
    
    # Bucle FOR desde 1 hasta N (inclusive)
    for i in range(1, n + 1):
        suma += i
        
    print(f"La suma de los primeros {n} números es: {suma}")

if __name__ == "__main__":
    suma_bucle()