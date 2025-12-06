# fichero pesetaseuros.py
# Este programa realiza la conversión de  pesetas a euros
def conversor():
    
    FACTOR_CONVERSION = 166.386
    try:
        pesetas = float(input("Introduce la cantidad en pesetas: "))
        euros = pesetas / FACTOR_CONVERSION
        print(f"{pesetas} pesetas equivalen a {euros:.2f} euros.")
    except ValueError:
        print("Error: Entrada no numérica.")
if __name__ == "__main__":
    conversor()