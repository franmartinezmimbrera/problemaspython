#fichero MCD.py
def calcular_mcd_script():
    print("Cálculo del MCD (Algoritmo de Euclides)")
    try:
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        
        if a < 0 or b < 0:
            print("Por favor, introduce números no negativos.")
            return

        original_a, original_b = a, b
        
        # Algoritmo de Euclides
        while b > 0:
            # En Python podemos intercambiar variables en una sola línea
            # a pasa a ser b, y b pasa a ser el resto de a/b
            a, b = b, a % b
            
        print(f"El MCD de {original_a} y {original_b} es: {a}")
        
    except ValueError:
        print("Error: Entrada no numérica.")

if __name__ == "__main__":
    calcular_mcd_script()