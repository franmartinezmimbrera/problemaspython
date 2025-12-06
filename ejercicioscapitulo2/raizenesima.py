# fichero raizenesima.py
# Este programa calcula la raíz n-ésima de un número
def raiz_enesima():
    try:
        base = float(input("Introduce el número (base): "))
        n = float(input("Introduce el índice de la raíz (n): "))
        
        if n == 0:
            print("No existe la raíz 0-ésima.")
            return
   
        resultado = base ** (1/n) # También se puede usar pow(base, 1/n)        
        print(f"La raíz {n}-ésima de {base} es: {resultado:.4f}")
        
    except ValueError:
        print("Error en los datos introducidos.")

if __name__ == "__main__":
    raiz_enesima()