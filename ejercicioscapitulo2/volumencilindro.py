# fichero volumencilindro.py
# Este programa calcula el volumen de un cilindro
import math

def volumen_cilindro():
    try:
        diametro = float(input("Introduce el diámetro del cilindro: "))
        altura = float(input("Introduce la altura del cilindro: "))
        
        radio = diametro / 2
        
        # Volumen = pi * r^2 * h
        volumen = math.pi * (radio ** 2) * altura
        
        print(f"El volumen del cilindro es: {volumen:.4f}")
    except ValueError:
        print("Error numérico.")

if __name__ == "__main__":
    volumen_cilindro()