# fichero costecoche.py 
# Este programa calcula el precio total de un coche
GANANCIA = 0.15 # 15%
IVA = 0.21      # 21%

try:
    coste_fabricacion = float(input("Introduce el coste de fabricación: "))
    # Calculamos el precio base con la ganancia
    precio_con_ganancia = coste_fabricacion * (1 + GANANCIA)
    # Aplicamos el IVA al precio anterior
    precio_final = precio_con_ganancia * (1 + IVA)
    
    print(f"\nCoste fabricación: {coste_fabricacion:.2f} €")
    print(f"Precio venta final (con 15% ganancia y 21% IVA): {precio_final:.2f} €")
    
except ValueError:
    print("Error: Debes introducir un valor numérico para el coste.")