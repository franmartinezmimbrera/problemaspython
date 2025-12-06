# fichero areatriangulo1.py 
# Calcula el área de un triáungulo rectángulo a partir de b y a
def area_triangulo_rect():
    try:
        base = float(input("Introduce la base: "))
        altura = float(input("Introduce la altura: "))
        area = (base * altura) / 2
        print(f"El área del triángulo rectángulo es: {area}")
    except ValueError:
        print("Error numérico.")
if __name__ == "__main__":
    area_triangulo_rect()