# fichero preciomedio.py 
# Este programa calcula el precio medio de un producto a partir de 3 precios

try:
    print("Por favor, introduce el precio del producto en 3 establecimientos distintos:")

    p1 = float(input("Precio en establecimiento 1: "))
    p2 = float(input("Precio en establecimiento 2: "))
    p3 = float(input("Precio en establecimiento 3: "))
    

    media = (p1 + p2 + p3) / 3

    print(f"\nEl precio medio del producto es: {media:.2f} €")
    
except ValueError:
    print("Error: Entrada inválida. Asegúrate de introducir números (ej: 12.50).")