# fichero areacuadrado.py 
# Este programa calcula el área de un cuadrado a partir de uno de sus lados

def area_cuadrado():
    try:
        lado = float(input("Introduce el valor del lado del cuadrado: "))
        area = lado ** 2  # Operador potencia en Python es **
        print(f"El área del cuadrado es: {area}")
    except ValueError:
        print("Error: Entrada no numérica.")

if __name__ == "__main__":
    area_cuadrado()