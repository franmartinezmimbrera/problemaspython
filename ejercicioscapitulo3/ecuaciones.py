# fichero ecuaciones.py 

import math

def resolver_ecuacion_segundo_grado():

    print("Resolución de ax^2 + bx + c = 0")
    a = float(input("Introduce a: "))
    b = float(input("Introduce b: "))
    c = float(input("Introduce c: "))
    
    if a == 0:
        print("Si a=0 no es una ecuación de segundo grado.")
        return

    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Dos soluciones reales: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"Una solución real doble: x = {x:.2f}")
    else:
        print("No existen soluciones reales (soluciones complejas).")

if __name__ == "__main__":
    resolver_ecuacion_segundo_grado()