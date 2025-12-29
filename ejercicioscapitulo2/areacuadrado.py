# fichero areacuadrado.py
# Programa que calcula el área de un cuadrado a partir de un lado

try:
    lado = float(input("Introduce el valor del lado del cuadrado: "))
    area = lado ** 2 
    print(f"El área del cuadrado es: {area}")

except ValueError:
    print("Error: Entrada no válida. Por favor, introduce un número (ej: 5 o 2.5).")