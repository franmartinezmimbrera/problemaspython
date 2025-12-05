# fichero tipotriangulo.py 
# Este programa calcula el tipo de triángulo en función de los lados
def tipo_triangulo():
    print("Introduce los tres lados del triángulo:")
    a = float(input("Lado A: "))
    b = float(input("Lado B: "))
    c = float(input("Lado C: "))
    
    if a == b and b == c:
        print("El triángulo es EQUILÁTERO.")
    elif a == b or a == c or b == c:
        print("El triángulo es ISÓSCELES.")
    else:
        print("El triángulo es ESCALENO.")

if __name__ == "__main__":
    tipo_triangulo()