#fichero sumaparesimpares.py
#Calcula la suma de 10 números pasados por teclado distinguiendo entre los pares e impares 
def sumar_pares_impares():
    numeros = []
    print("Introduce 10 números:")
    
    # Lectura de datos
    for i in range(10):
        val = int(input(f"Dato {i+1}: "))
        numeros.append(val)
        
    suma_pares = 0
    suma_impares = 0
    
    for num in numeros:
        if num % 2 == 0:
            suma_pares += num
        else:
            suma_impares += num
            
    print(f"Suma de PARES: {suma_pares}")
    print(f"Suma de IMPARES: {suma_impares}")

if __name__ == "__main__":
    sumar_pares_impares()