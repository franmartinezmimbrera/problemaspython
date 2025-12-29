# fichero parimpar.py
# Programa que verifica si un número es par o impar
try:
    numero = int(input("Introduce un número entero: "))
    
    if numero % 2 == 0:
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")
        
except ValueError:
    print("Error: Debes introducir un número entero válido.")