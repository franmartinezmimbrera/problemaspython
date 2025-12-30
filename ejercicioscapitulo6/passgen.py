# fichero passgen.py
# Generador de contraseñas aleatorias seguras
# Utiliza el módulo 'secrets' (CSPRNG).
import secrets
import string
# Definimos el conjunto de caracteres permitidos
CHARSET = string.ascii_letters + string.digits + "!@#$%^&*()"
def generar_contrasena(longitud):
    # secrets.choice(CHARSET) elige un carácter de forma segura
    # Repetimos el proceso 'longitud' veces y unimos en una cadena
    return "".join(secrets.choice(CHARSET) for _ in range(longitud))
if __name__ == "__main__":
    try:
        entrada = input("Introduce la longitud deseada: ")
        longitud = int(entrada)        
        if longitud <= 0:
            print("Error: La longitud debe ser mayor que 0.")
        else:
            print("Generando contraseña...", end=" ")
            password = generar_contrasena(longitud)
            print(f"\n{password}")
            
    except ValueError:
        print("\nError: Debes introducir un número entero.")