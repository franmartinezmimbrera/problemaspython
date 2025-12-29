# fichero areatriangulo2.py 
# Calcula el área de un triángulo equilátero a partir de uno de sus lados

import math

try:

    lado = float(input("Introduce el lado del triángulo equilátero: "))
    area = (math.sqrt(3) / 4) * (lado ** 2)

    print(f"El área del triángulo equilátero es: {area:.4f}")

except ValueError:
    print("Error: Entrada no válida. Por favor, introduce un número.")