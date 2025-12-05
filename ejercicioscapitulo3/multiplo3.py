#fichero multiplo3.py
def multiplo_tres_y_par():
    try:
        numero = int(input("Introduce un número: "))
        
        # Usamos el operador lógico 'and'
        if (numero % 3 == 0) and (numero % 2 == 0):
            print(f"El número {numero} es múltiplo de 3 y PAR.")
        else:
            print(f"El número {numero} NO cumple ambas condiciones.")
            
    except ValueError:
        print("Entrada no válida.")

if __name__ == "__main__":
    multiplo_tres_y_par()