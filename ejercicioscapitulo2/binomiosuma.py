# fichero binomiosuma.py
# Este programa calcula el binomio de suma de (a + b) al cuadrado 
try:
    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: ")) 
    # Fórmula (a^2 + b^2 + 2ab)    
    resultado = (a ** 2) + (b ** 2) + (2 * a * b)
    print(f"El resultado de ({a} + {b})^2 es: {resultado}")
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce números.")