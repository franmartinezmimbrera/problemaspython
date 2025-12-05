# -*- coding: iso-8859-15 -*-
# fichero capturar.py
# Este programa recopila datos del usuario mediante preguntas

def capturar_datos():
    
    nombre = input("Introduce tu nombre (texto): ")
    edad = int(input("Introduce tu edad (entero): "))
    altura = float(input("Introduce tu altura en metros (decimal): "))
    
    print("\n Datos Recopilados")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Altura: {altura} m")

if __name__ == "__main__":
    try:
        capturar_datos()
    except ValueError:
        print("Error: Asegúrate de introducir números válidos para edad y altura.")
