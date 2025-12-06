# fichero pulgadasmilimetros.py 
# Este programa cambia pulgadas por milímetros
def pulgadas_a_mm():
    FACTOR = 25.4
    try:
        pulgadas = float(input("Introduce valor en pulgadas: "))
        milimetros = pulgadas * FACTOR
        print(f"{pulgadas} pulgadas son {milimetros} milímetros.")
    except ValueError:
        print("Error de entrada.")
if __name__ == "__main__":
    pulgadas_a_mm()