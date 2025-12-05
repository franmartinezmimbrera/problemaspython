# -*- coding: iso-8859-15 -*-
# fichero areatriangulo2.py 
# Calcula el área de un triáungulo equilátero a partir de uno de sus lados
import math

def area_triangulo_equi():
    
    try:
        lado = float(input("Introduce el lado del triángulo equilátero: "))
        
        # Fórmula: (raiz(3) / 4) * lado^2
        area = (math.sqrt(3) / 4) * (lado ** 2)
        
        print(f"El área del triángulo equilátero es: {area:.4f}")
    except ValueError:
        print("Error numérico.")

if __name__ == "__main__":
    area_triangulo_equi()