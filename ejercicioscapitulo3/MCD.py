# fichero MCD.py
# Programa que calcula el Máximo Común Divisor (Algoritmo de Euclides)

try:
    a = int(input("Introduce el primer número: "))
    
    b = int(input("Introduce el segundo número: "))
    
    if a < 0 or b < 0:
        print("Error: Por favor, introduce números enteros positivos.")
    else:
        original_a, original_b = a, b
        
        # Algoritmo de Euclides
        # Se repite hasta que el resto (b) sea 0
        while b > 0:
            a, b = b, a % b
            
        # Cuando b es 0, 'a' contiene el MCD
        print(f"El MCD de {original_a} y {original_b} es: {a}")
        
except ValueError:
    
    print("Error: Entrada no válida. Introduce números enteros.")