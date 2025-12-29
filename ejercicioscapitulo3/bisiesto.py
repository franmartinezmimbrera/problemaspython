# fichero bisiesto.py
# Programa que comprueba si un año es bisiesto
try:
    anio = int(input("Introduce un año: "))    
    # Condición de bisiesto:
    # Divisible entre 4 Y NO divisible entre 100
    # O
    # Divisible entre 400
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"El año {anio} ES bisiesto.")
    else:
        print(f"El año {anio} NO es bisiesto.")
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce un año (número entero).")