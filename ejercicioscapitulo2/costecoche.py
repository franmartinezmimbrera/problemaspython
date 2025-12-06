# fichero costecoche.py 
# Este programa calcula el precio total de un coche

def coste_coche():
    
    GANANCIA = 0.15 # 15%
    IVA = 0.21      # 21%
    try:
        coste_fabricacion = float(input("Introduce el coste de fabricación: "))
        precio_con_ganancia = coste_fabricacion * (1 + GANANCIA)
        precio_final = precio_con_ganancia * (1 + IVA)
        
        print(f"Coste fabricación: {coste_fabricacion:.2f} €")
        print(f"Precio venta final (con ganancia e IVA): {precio_final:.2f} €")
        
    except ValueError:
        print("Error numérico.")

if __name__ == "__main__":
    coste_coche()