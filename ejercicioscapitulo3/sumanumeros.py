# fichero sumanumeros.py
#  Este programa calcula la suma de los números introducidos por teclado mientras no se introduzca el número -50 

def sumar_hasta_parada():
    suma_total = 0
    numero = 0
    NUMERO_PARADA = -50
    
    print(f"Introduce números para sumar. Escribe {NUMERO_PARADA} para terminar.")
    
    while True:
        try:
            numero = int(input("Introduce número: "))
            if numero == NUMERO_PARADA:
                break # Salimos del bucle
            
            suma_total += numero
        except ValueError:
            print("Por favor, introduce un número válido.")
            
    print(f"La suma total acumulada es: {suma_total}")

if __name__ == "__main__":
    sumar_hasta_parada()