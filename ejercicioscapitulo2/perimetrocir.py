# fichero perimetrocir.py
# Este programa calcula el perímetro de una circunferencia
import math # Librería matemática para usar el valor de PI
try:
    radio = float(input("Introduce el radio de la circunferencia: "))
    perimetro = 2 * math.pi * radio
    print(f"El perímetro de la circunferencia es: {perimetro:.4f}")
    
except ValueError:
    # Gestión de errores
    print("Error: Entrada inválida. Por favor, introduce un número.")