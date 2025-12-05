# fichero alturatriangulo.py
# Este programa calcula la altura de un triángulo equilatero
import math

def altura_triangulo_equi():
    try:
        lado = float(input("Introduce el lado del triángulo equilátero: "))
        
        # h = (raiz(3) * lado) / 2
        altura = (math.sqrt(3) * lado) / 2
        
        print(f"La altura del triángulo es: {altura:.4f}")
    except ValueError:
        print("Error numérico.")

if __name__ == "__main__":
    altura_triangulo_equi()