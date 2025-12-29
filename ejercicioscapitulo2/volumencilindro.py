# fichero volumencilindro.py
# Este programa calcula el volumen de un cilindro
import math
try:
    diametro = float(input("Introduce el diámetro del cilindro: "))
    altura = float(input("Introduce la altura del cilindro: "))
    # Calcular radio (diámetro / 2)
    radio = diametro / 2
    # Calcular volumen (pi * r^2 * h)
    volumen = math.pi * (radio ** 2) * altura
    print(f"El volumen del cilindro es: {volumen:.4f}")
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce números.")