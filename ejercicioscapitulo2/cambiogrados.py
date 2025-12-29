# fichero cambiogrados.py 
# Este programa cambia grados centígrados por Fahrenheit

try:
    celsius = float(input("Introduce grados Celsius: "))    
    fahrenheit = (9/5 * celsius) + 32    
    print(f"{celsius} ºC equivalen a {fahrenheit:.2f} ºF")
    
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce un número.")