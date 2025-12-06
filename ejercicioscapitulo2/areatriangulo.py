# fichero areatriangulo.py 
# Este programa calcula el área de un triáungulo a partir de sus lados mediante la fórmula de Herón
import math

def area_heron():
    
    print("Introduce los 3 lados del triángulo:")
    try:
        l1 = float(input("Lado 1: "))
        l2 = float(input("Lado 2: "))
        l3 = float(input("Lado 3: "))
        
        # Semiperímetro
        sp = (l1 + l2 + l3) / 2
        
        # Fórmula de Herón
        # Comprobamos que el valor dentro de la raíz sea positivo (triángulo válido)
        radicando = sp * (sp - l1) * (sp - l2) * (sp - l3)
        
        if radicando < 0:
            print("Los lados introducidos no forman un triángulo válido.")
        else:
            area = math.sqrt(radicando)
            print(f"El área del triángulo es: {area:.4f}")
            
    except ValueError:
        print("Error numérico.")

if __name__ == "__main__":
    area_heron()