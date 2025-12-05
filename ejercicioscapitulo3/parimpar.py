#fichero parimpar.py
def verificar_paridad():
    try:
        numero = int(input("Introduce un número entero: "))
        
        if numero % 2 == 0:
            print(f"El número {numero} es PAR.")
        else:
            print(f"El número {numero} es IMPAR.")
            
    except ValueError:
        print("Error: Debes introducir un número entero válido.")

if __name__ == "__main__":
    verificar_paridad()