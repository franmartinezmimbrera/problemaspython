# fichero areatriangulo2.py 
import math

def area_heron(a, b, c):
    # Semiperímetro
    s = (a + b + c) / 2
    # Fórmula de Herón: raiz(s * (s-a) * (s-b) * (s-c))
    try:
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    except ValueError:
        return -1 # Retornamos -1 si los lados no forman un triángulo válido

if __name__ == "__main__":
    print("Introduce los lados del triángulo:")
    l1 = float(input("Lado A: "))
    l2 = float(input("Lado B: "))
    l3 = float(input("Lado C: "))
    
    resultado = area_heron(l1, l2, l3)
    
    if resultado != -1:
        print(f"El área del triángulo es: {resultado:.2f}")
    else:
        print("Los lados proporcionados no forman un triángulo válido.")