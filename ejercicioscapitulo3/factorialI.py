# fichero factorialI.py
#Calcula el factorial de un número entero no negativo de forma iterativa

def factorial_iterativo(n):
    if n < 0:
        return None # No existe factorial de negativos
    if n == 0:
        return 1
        
    resultado = 1
    # Multiplicamos desde 1 hasta n
    for i in range(1, n + 1):
        resultado *= i
        
    return resultado

if __name__ == "__main__":
    num = int(input("Introduce un número para calcular su factorial: "))
    res = factorial_iterativo(num)
    if res is not None:
        print(f"{num}! = {res}")
    else:
        print("El número no puede ser negativo.")