# fichero pulgadasmilimetros.py 
# Este programa cambia pulgadas por milímetros
FACTOR = 25.4
try:
    pulgadas = float(input("Introduce el valor en pulgadas: "))
    milimetros = pulgadas * FACTOR
    print(f"{pulgadas} pulgadas son {milimetros} milímetros.")
    
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce un número.")