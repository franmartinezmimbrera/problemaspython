# fichero binomiosuma.py
# Este programa calcula el binomio de suma de a+b al cuadrado 

def binomio_cuadrado():
    print("Cálculo de (a + b)^2")
    try:
        a = float(input("Introduce a: "))
        b = float(input("Introduce b: "))
        
        # Podemos hacerlo directamente: (a+b)**2
        # O desglosado: a^2 + b^2 + 2ab
        resultado = (a ** 2) + (b ** 2) + (2 * a * b)
        
        print(f"El resultado del binomio al cuadrado es: {resultado}")
        
    except ValueError:
        print("Error numérico.")

if __name__ == "__main__":
    binomio_cuadrado()