# fichero preciomedio.py 
# Este programa calcula el precio medio de un producto

def precio_medio():

    try:
    
        print("Introduce el precio del producto en 3 establecimientos:")
    
        p1 = float(input("Precio 1: "))
        p2 = float(input("Precio 2: "))
        p3 = float(input("Precio 3: "))
        
        media = (p1 + p2 + p3) / 3
    
        print(f"El precio medio del producto es: {media:.2f} €")
        
    except ValueError:
        print("Error en la entrada de datos.")

if __name__ == "__main__":
    precio_medio()