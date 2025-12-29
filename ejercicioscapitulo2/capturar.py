# fichero capturar.py
# Este programa recopila datos del usuario de forma segura

try:

    nombre = input("Introduce tu nombre (texto): ")    
    edad = int(input("Introduce tu edad (entero): "))
    altura = float(input("Introduce tu altura en metros (decimal con punto): "))

    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Altura: {altura} m")

except ValueError:
    print("\n[!] ERROR CRÍTICO:")
    print("Has introducido un texto donde se esperaba un número.")
    print("Por favor, reinicia el programa e introduce datos válidos (ej: edad 25, altura 1.75).")