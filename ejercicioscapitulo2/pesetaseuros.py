# fichero pesetaseuros.py
# Este programa realiza la conversión de cantidades en pesetas a cantidades en euros

def conversor():
    FACTOR_CONVERSION = 166.386
    
    try:
        pesetas = float(input("Introduce la cantidad en Pesetas: "))
        euros = pesetas / FACTOR_CONVERSION
        # .2f formatea a 2 decimales
        print(f"{pesetas} pesetas equivalen a {euros:.2f} Euros.")
    except ValueError:
        print("Error: Entrada no numérica.")

if __name__ == "__main__":
    conversor()