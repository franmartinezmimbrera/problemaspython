# fichero cambiagrados.py 
# Este programa cambia grados centígrados por fahrenheit

def celsius_a_fahrenheit():
    try:
        celsius = float(input("Introduce grados Celsius: "))
        # Fórmula: (9/5 * C) + 32
        fahrenheit = (9/5 * celsius) + 32
        print(f"{celsius} ºC equivalen a {fahrenheit:.2f} ºF")
    except ValueError:
        print("Error de entrada.")

if __name__ == "__main__":
    celsius_a_fahrenheit()