# fichero raizcuadrada.py
# Este programa calcula la raíz cuadrada de un número
import math
try:
    numero = float(input("Introduce un número: "))
    if numero < 0:
        print("Error: No se puede calcular la raíz cuadrada real de un número negativo.")
    else:
        raiz = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es {raiz:.4f}")
except ValueError:
    print("Error: Entrada inválida. Por favor, introduce un número.")