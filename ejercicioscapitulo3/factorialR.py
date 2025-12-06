#fichero factorialR.py
#Calcula el factorial de un número entero no negativo de forma recursiva. 

def factorial_recursivo(n):
    if n < 0:
        return None
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Llamada recursiva
    return n * factorial_recursivo(n - 1)

if __name__ == "__main__":
    num = int(input("Introduce un número (recursivo): "))
    print(f"Factorial: {factorial_recursivo(num)}")