# fichero areatriangulo1.py 
# Calcula el área de un triángulo rectángulo a partir de base y altura
try:
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    area = (base * altura) / 2
    print(f"El área del triángulo rectángulo es: {area}")
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce números.")