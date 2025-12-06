# fichero areacircunferencia.py
import math
def area_circunferencia(radio):
    if radio < 0:
        return None
    return math.pi * (radio ** 2)
if __name__ == "__main__":
    r = float(input("Introduce el radio: "))
    area = area_circunferencia(r)
    if area is not None:
        print(f"El Área de la circunferencia es: {area:.4f}")
    else:
        print("El radio no puede ser negativo.")