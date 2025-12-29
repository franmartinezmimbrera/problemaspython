# fichero ladotriangulo.py
# Este programa calcula el valor del cateto 'a' de un triángulo rectángulo dados la hipotenusa 'h' y el otro cateto 'b'
import math
try:
    h = float(input("Introduce la hipotenusa (h): "))
    b = float(input("Introduce el otro cateto (b): "))       
    if h <= b:
        print("Error: La hipotenusa debe ser > que el cateto.")
    else:
        a = math.sqrt(h**2 - b**2)
        print(f"El valor del cateto 'a' es: {a:.4f}")
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce números.")