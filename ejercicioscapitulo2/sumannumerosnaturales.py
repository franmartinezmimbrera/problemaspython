# fichero sumannumerosnaturales.py
# Este programa calcula la suma de los "n" primeros números naturales 

try:
    
    n = int(input("Introduce un número entero 'n': "))
    
    if n < 0:
        print("Por favor, introduce un número entero positivo.")
    else:
        # Aplicamos la fórmula de Gauss: n * (n + 1) / 2
        # Usamos // para asegurar que la división es entera
        suma = (n * (n + 1)) // 2
        
        print(f"La suma de los primeros {n} números naturales es: {suma}")
        
except ValueError:
    print("Error: Debes introducir un número entero válido.")