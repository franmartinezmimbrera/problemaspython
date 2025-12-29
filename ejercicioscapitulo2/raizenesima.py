# fichero raizenesima.py
# Este programa calcula la raíz n-ésima de un número
try:
    base = float(input("Introduce el número (base): "))
    n = float(input("Introduce el índice de la raíz (n): "))
    if n == 0:
        print("Error: No existe la raíz 0-ésima.")
    else:
        resultado = base ** (1/n) 
        print(f"La raíz {n}-ésima de {base} es: {resultado:.4f}")
except ValueError:
    print("Error: Entrada no válida. Asegúrate de introducir números.")