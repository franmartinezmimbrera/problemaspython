# fichero ladotriangulo.py
# Este programa calcula el valor del lado a de un triangulo rectángulo usando el valor del lado b y la hipotenusa h 
import math

def calcular_cateto():
    print("Cálculo del cateto 'a' (h^2 = a^2 + b^2)")
    try:
        h = float(input("Introduce la hipotenusa (h): "))
        b = float(input("Introduce el otro cateto (b): "))
        
        if h <= b:
            print("La hipotenusa debe ser mayor que el cateto.")
            return

        # a = raiz(h^2 - b^2)
        a = math.sqrt(h**2 - b**2)
        
        print(f"El valor del cateto 'a' es: {a:.4f}")
    except ValueError:
        print("Error numérico.")

if __name__ == "__main__":
    calcular_cateto()