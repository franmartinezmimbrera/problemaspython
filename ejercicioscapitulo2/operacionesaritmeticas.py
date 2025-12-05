# -*- coding: iso-8859-15 -*-
# fichero operacionesaritmeticas.py 
# Este programa realiza operaciones aritméticas dados 2 números
       
def operaciones_basicas():

    try:
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        
        print("Resultados ")
        print(f"Suma:           {n1} + {n2} = {n1 + n2}")
        print(f"Resta:          {n1} - {n2} = {n1 - n2}")
        print(f"Multiplicación: {n1} * {n2} = {n1 * n2}")
        
        if n2 != 0:
            print(f"División:  {n1} / {n2} = {n1 / n2}")
        else:
            print("División: No se puede dividir por cero.")
            
    except ValueError:
        print("Debes introducir números válidos.")

if __name__ == "__main__":
    operaciones_basicas()