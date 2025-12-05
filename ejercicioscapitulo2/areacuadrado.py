# -*- coding: iso-8859-15 -*-
# fichero areacuadrado.py 
# Programa que calcula el área de un cuadrado a partir de un lado
def area_cuadrado():
    try:
        lado = float(input("Introduce valor del lado del cuadrado: "))
        area = lado ** 2  # Operador potencia en Python es **
        print(f"El área del cuadrado es: {area}")
    except ValueError:
        print("Error: Entrada no numérica.")
if __name__ == "__main__":
    area_cuadrado()