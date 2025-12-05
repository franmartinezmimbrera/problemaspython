# fichero sumannumerosnaturales.py
#  Este programa calcula la suma de los "n" primeros números naturales 

def suma_gauss():
    try:
        n = int(input("Introduce un número entero 'n': "))
        
        if n < 0:
            print("Por favor, introduce un número positivo.")
            return

        # Aplicamos la fórmula: n * (n + 1) / 2
        # Usamos // para división entera
        suma = (n * (n + 1)) // 2
        
        print(f"La suma de los primeros {n} números naturales es: {suma}")
        
    except ValueError:
        print("Debes introducir un número entero.")

if __name__ == "__main__":
    suma_gauss()