# fichero perimetrocir.py
# Este programa calcula el perímetro de una circunferencia
import math # Necesario para usar math.pi

def perimetro_circunferencia():
    
    try:
        radio = float(input("Introduce el radio de la circunferencia: "))
        perimetro = 2 * math.pi * radio
        
        print(f"El perímetro es: {perimetro:.4f}")
    except ValueError:
        print("Entrada inválida.")

if __name__ == "__main__":
    perimetro_circunferencia()