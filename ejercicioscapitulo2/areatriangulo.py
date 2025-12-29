# fichero areatriangulo.py 
# Este programa calcula el área de un triángulo a partir de sus lados mediante la fórmula de Herón
import math

try:
    print("Por favor, introduce los 3 lados del triángulo:")
    l1 = float(input("Lado 1: "))
    l2 = float(input("Lado 2: "))
    l3 = float(input("Lado 3: "))
    
    # Calcular el semiperímetro (s)
    sp = (l1 + l2 + l3) / 2
    
    # Calcular el radicando de la fórmula de Herón: s(s-a)(s-b)(s-c)
    radicando = sp * (sp - l1) * (sp - l2) * (sp - l3)
    
    if radicando < 0:
        print("Error: Los lados introducidos no forman un triángulo válido (desigualdad triangular).")
    else:
        area = math.sqrt(radicando)
        print(f"El área del triángulo es: {area:.4f}")
        
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce números.")