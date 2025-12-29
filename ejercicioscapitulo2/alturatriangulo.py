# fichero alturatriangulo.py
# Este programa calcula la altura de un triángulo equilátero
import math
try:
    lado = float(input("Introduce el lado del triángulo equilátero: "))
    
    if lado <= 0:
        print("Error: El lado debe ser mayor que 0.")
    else:
        altura = (math.sqrt(3) * lado) / 2
        print(f"La altura del triángulo es: {altura:.4f}")    
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce un número.")