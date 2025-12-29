# fichero multiplo3.py
# Programa que verifica si un número es múltiplo de 3 y PAR a la vez
try:
    numero = int(input("Introduce un número entero: "))    
    # Múltiplo de 3 AND Múltiplo de 2 (Par)
    # Matemáticamente, esto equivale a ser múltiplo de 6
    if (numero % 3 == 0) and (numero % 2 == 0):
        print(f"El número {numero} es múltiplo de 3 y PAR.")
    else:
        print(f"El número {numero} NO cumple ambas condiciones.")        
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce un número entero.")